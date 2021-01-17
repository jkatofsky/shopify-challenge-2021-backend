#!/usr/bin/python3

import argparse
import requests
from os import path
import base64

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('repo_address', help="The address of the image repository.")
    parser.add_argument('action', help="The action you wish to complete. \
                         One of \"upload\", \"download\", \"update\", or \"delete\".")
    parser.add_argument('--i', help="The location of the input image.")
    parser.add_argument('--o', help="The location to save a downloaded image.")
    parser.add_argument('--id', help="The ID of an image in the repository.")

    args = parser.parse_args()

    if not args.action in ['upload', 'download', 'delete', 'update']:
        parser.error("Invalid action.")

    if not args.action == 'upload' and not args.id:
        parser.error("You must provide an image ID.")

    if args.action in ['upload', 'update'] and not args.i:
        parser.error("You must provide a source for the image.")

    if args.action == 'download' and not args.o:
        parser.error("You must provide an output path for the image.")

    if args.i and not path.isfile(args.i):
        parser.error("Invalid image source.")

    if args.o and not path.exists(path.dirname(path.abspath(args.o))):
        parser.error("Invalid image output path.")


    #TODO: these conditionals seem like they can be simplified
    repo_address = f'{args.repo_address}/images'

    if args.action in ['upload', 'update']:
        with open(args.i, "rb") as image_file:
            encoded_img_str = base64.b64encode(image_file.read())

            if args.action == 'upload':
                response = requests.post(repo_address, 
                                    json={'image': encoded_img_str})
            else:
                response = requests.put(repo_address, 
                                    json={'image': encoded_img_str, 'id': args.id})

    elif args.action == 'delete':
        response = requests.delete(repo_address, json={'id': args.id})
    
    else:
        response = requests.get(repo_address, json={'id': args.id})


    if not response.status_code == 200:
        print(response.text)
    if response.headers['content-type'].startswith('image'):
        with open(args.o, 'wb') as image_fp:
            image_fp.write(response.content)
    else:
        data = response.json()
        print('Action \"%s\" successfully completed to image %s' % (args.action, data['id']))


if __name__ == "__main__":
    main()