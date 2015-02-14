#!/usr/bin/env
sudo service nginx start
gunicorn -c gunicorn.conf.py itt.wsgi --daemon
nodejs nodejs/server.js