# flaskr.py from flask microblog tutorial (flask.pocoo.org)
# by Marshall Ehlinger

# Imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
from context import closing

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
	
def init_db():
	with closing(connect_db()) as db:
		with app.open_resources('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit())	

@app.before_request
def before_request():
	g.db = connect_db()
	
@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

if __name__ == '__main__':
	app.run()
	