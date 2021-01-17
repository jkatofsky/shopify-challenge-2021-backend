import argparse
import requests
import os
import base64
from io import BytesIO # will be used to save images when there's a get request


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('repo_address', help="You must provide the address of the image repository.")
    parser.add_argument('action', help="You must provide the action you wish to complete.")
    parser.add_argument('--img_path')
    parser.add_argument('--img_id')

    args = parser.parse_args()

    if not args.action in ['upload', 'download', 'delete', 'update']:
        parser.error("Invalid action.")

    if not args.action == 'upload' and not args.img_id:
        parser.error("You must provide an image ID.")

    if args.action in ['upload', 'update'] and not args.img_path:
        parser.error("You must provide an image path.")

    if not os.path.exists(args.img_path):
        parser.error("Invalid image path.")


    #TODO: these conditionals can maybe be improved
    if args.action in ['upload', 'update']:
        with open(args.img_path, "rb") as image_file:
            encoded_img_str = base64.b64encode(image_file.read())

            if args.action == 'upload':
                response = requests.post(args.repo_address, 
                                    json={'image': encoded_img_str})
            else:
                response = requests.put(args.repo_address, 
                                    json={'image': encoded_img_str, 'id': args.img_id})

    elif args.action == 'delete':
        response = requests.delete(args.repo_address, json={'id': args.img_id})
    
    else:
        response = requests.get(args.repo_address, json={'id': args.img_id})

    # TODO: handle the response


if __name__ == "__main__":
    main()