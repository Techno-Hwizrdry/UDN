# UDN
This is a small django web app that collects information about participants and lists each participant along with their information.

# Prerequisites
This Django application requires python3, python3-pip, and python-virutalenv.  Therefore, all 3 must be installed first
before the app can be used.  They can be installed on a Debian based linux machine, like so:

`sudo apt-get update && sudo apt-get install python3 python3-pip && pip3 install virtualenv`

# Quick Start
Once the prerequisites have been satisfied, git clone this repo, cd into it, and activate the virtual environment:

`cd /path/to/udn && source udnenv/bin/activate`

Then, to start the Django development server, cd into the subdirectory called 'udn' and run the following command:

`cd udn/ && python3 manage.py runserver 8000`
