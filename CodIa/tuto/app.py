from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
import os
UPLOAD_FOLDER = 'tuto/IA'
ALLOWED_EXTENSIONS = set(['txt', 'py'])
app=Flask(__name__)
app.debug=True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['BOOTSTRAP_SERVE_LOCAL']=True

from flask.ext.bootstrap import Bootstrap
Bootstrap(app)

from flask.ext.script import Manager
manager=Manager(app)


import os.path
def mkpath(p):
	return os.path.normpath(
		os.path.join(
			os.path.dirname(__file__),
			p))


from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
	'sqlite:///'+mkpath('../CodIA.db'))
db=SQLAlchemy(app)

app.config['SECRET_KEY']="f5e63d01-f3a7-48d1-af81-bb0c3f3b458a"

from flask.ext.login import LoginManager
login_manager=LoginManager(app)




