# symmetrical-happiness
a simple search to find web project implemented using python-flask and bulma css

## How to run?
-`git clone -----url----`\
-`cd symmetrical-happiness`
### venv
if existing venv setup shows errors\
-`python3 -m venv venv`\
-`source venv/bin/activate`\
-`pip3 install -r requirements.txt`
### mysql pre-setup[in BASH]
-`cd symmetrical-happiness`\
-`sudo mysql`\
-`source db.sql`
### config setup
edit database details in config
### run
-`cd symmetrical-happiness`\
-`python3 main.py`


## how this is done
- a simple search page designed using bulma
- ajax to fetch similiar typos
- suitable choice is passed to backed in GET
- appointments are retrived

## notice
- not optimised for mobile
- cdn is used for javascript libraries
- blueprints used

## libraries used
- animejs
- jquery
- google fonts
- fontawesome
- bulma css

## mysql tables
- users
- doctors
- events
