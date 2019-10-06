#!/bin/bash
pip freeze > requirements.txt
# heroku create aws-management-test
# git remote -v 
# pip install gunicorn
git add .
git commit -m "version 0.1.1"
git push origin master
git push heroku master