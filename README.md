# Dolt Flask API
Project to build an API that interacts with dolt repos

## Use Case(s)
Dolt is great for versioning of data which can come in handy when cleaning or sorting data, as it brings the power of git to databases. The hope for this API is that it enables whomever uses it to query data from dolthub database repositories, allowing someone to view previous commits and branches of a database.

## Built with
* Python 3 with Flask and the official Dolthub DoltPy PIP package

## Using the API
**Make sure Python 3 and PIP are installed**

* Option 1
    * Run `serve.sh` which creates and activates an environment, installs dependencies and gets the API up

* Option 2
    * Create an environment `python3 -m venv env`
    * Activate the environment `source env/bin/activate`
    * Install dependencies `pip3 install -r requirements.txt`
    * Export Flask environment variable `FLASK_APP=api`
    * Run flask app `flask run`