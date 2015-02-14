@echo off
start "Django server" /d C:\Users\CJ\Projects\itt python manage.py runserver
start "Nodejs server" /d C:\Users\CJ\Projects\itt\nodejs node server.js