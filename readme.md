COIAPI :: Piston
================
django-piston based API example backed by MongoDB.

Setup
------

* create a virtualenv
* pip install -r requirements.txt
* (optional) configure mongodb host in settings.py
* python manage.py runserver

Usage
-----

curl localhost:8000/api/trials/
curl localhost:8000/api/trials/<ID>/
