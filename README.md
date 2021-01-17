# Image Repository

My submission for the Shopify 2021 Summer Backend Developer Intern Challenge. Consists of a basic [Flask](https://flask.palletsprojects.com/en/1.1.x/)/[mongoengine](http://mongoengine.org/) CRUD "repository" for images and a client script (making heavy use of the [argparse](https://docs.python.org/3/library/argparse.html) and [requests](https://requests.readthedocs.io/en/master/) modules) that provides a nice command line interface for interacting with the repository.

## Usage

Whether you're hosting the repository or using the command line tool, it starts with cloning this repo.

```bash
git clone https://github.com/jkatofsky/shopify-challenge-2021-backend.git
```

### Repository

To run a repository, you need to have [mongoDB](https://docs.mongodb.com/manual/installation/) installed and have a mongod instance running on localhost, port 27017.

Then, you can start the server in development mode as follows:

```bash
cd repo
pip3 install -r requirements.txt
python3 app.py
```

Of course, in a production environment, you should use a [production server](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/#run-with-a-production-server).


### Client

Make sure you have the `requests` module installed. Then, you can run the script to interact with any repository. To see the usage of the script, run

```bash
python3 img_repo.py --help
```

To make the script more useful, you can also [add it to your path to make it excecutable from any directory](https://www.geeksforgeeks.org/run-python-script-from-anywhere-in-linux/).

## Possible Improvements

This is admittedly a pretty simple project. I was under a time crunch (McGill winter semester starts sooner than other Canadian schools'), so I figured I would attempt something limited in scope to make sure that it worked. Below are some features that I would have explored if I had more time.

- Image metadata: filename, titles, descriptions, keywords, etc. 
  - Allow API queries based on those criteria, and save images locally with existing filename.
  - Add API queries that returns metadata only.
- Querying for multiple images at once.
- Image collections.
- User auth (through what method?)
  - `Image`s get foreign key to `User`.
  - `Image`s get public/private bool field, anyone can access the former.