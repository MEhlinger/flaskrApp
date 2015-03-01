# flaskr.py from flask micorblog tutorial (flask.pocoo.org)
# by Marshall Ehlinger

# Imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash

# Configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True #REMEMBER TO DISABLE DEBUG ON ANY PRODUCTION SYSTEM.... HACKABLE
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# Create the application!
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])
	
if __name__ == '__main__':
	app.run()
	