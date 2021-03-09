#!/bin/bash

python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 app.py
export FLASK_APP=api
flask run