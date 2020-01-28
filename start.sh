#!/bin/bash
app="flaskboard"

pipenv run gunicorn -w 1 -b 0.0.0.0:5000 wsgi:app
firefox 0.0.0.0:5000
