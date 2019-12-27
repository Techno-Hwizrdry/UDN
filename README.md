# UDN
This is a small django web app that collects information about participants and lists each participant along with their information.

# Prerequisites
This Django application requires python3, python3-pip, and python-virutalenv.  Since this document assumes that UDN
will run on your local machine (for development only), all 3 must be installed on your local machine before the app can be used.
To serve this document in a producton (or production-like) environment, please refer to the instructions to serve via [Nginx](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html) or [Apache](https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/modwsgi/#serving-files).

The prerequisites can be installed on a Debian based linux machine, like so:

`sudo apt-get update && sudo apt-get install python3 python3-pip && pip3 install virtualenv`

Once those prerequisites have been installed, git clone this repo, cd into it, and activate the virtual environment:

`cd /path/to/udn && source udnenv/bin/activate`

Then install Django by running this command:

`pip3 install -r requirements.txt`

# Quick Start
Then, to start the Django development server, cd into the subdirectory called 'udn' and run the following command:

`cd udn/ && python3 manage.py runserver 8000`

On your local machine, open up your prefered web browser and navigate to http://127.0.0.1:8000/participant_info to start using the web app.
