#!/bin/sh

gunicorn -w 4 -b 127.0.0.1:4000 flask_server:app

