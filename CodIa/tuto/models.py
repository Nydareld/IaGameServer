from .app import db
from flask.ext.login import UserMixin
from .app import login_manager


class User(db.Model, UserMixin):
	pseudo = db.Column(db.String(100),primary_key=True)
	usermail = db.Column(db.String(100))
	username = db.Column(db.String(50))
	usersurname = db.Column(db.String(50))
	password = db.Column(db.String(64))
	score= db.Column(db.Integer)
	
	
	def get_id(self):
		return self.pseudo
	
	def __repr__(self):
		return "%s - %s - %s" % (self.pseudo, self.username, self.usermail)


def getUser(pseudo):
	return db.session.query(User).filter(User.pseudo==pseudo).first()

@login_manager.user_loader
def load_user(username):
	return User.query.get(username)

class Ia(db.Model):
	id		=db.Column(db.Integer, primary_key=True)
	user_pseudo =db.Column(db.String(100)) 
	name    =db.Column(db.String(100))  

def removeIa(filename):
	s = db.session()
	m=s.query(Ia).filter(Ia.name==filename).all()
	for c in m:
   		db.session.delete(c)
