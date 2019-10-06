#!/bin/bash
pip freeze > requirements.txt
git add .
# git add README.md environment.yml plot_shapefile.py correlation_plot.py app.py
git commit -m "version 0.1"
git push origin master
# git push heroku master