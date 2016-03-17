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
# class Singer(db.Model):
# 	id		=db.Column(db.Integer, primary_key=True)
# 	name 	=db.Column(db.String(100))
# 	def __repr__(self):
# 		return "<Singer (%d) %s>" % (self.id,self.name)






# class Genre (db.Model):
# 	id		=db.Column(db.Integer, primary_key=True)
# 	name 	=db.Column(db.String(100))
	
# 	def __repr__(self):
# 		return "<Singer (%d) %s>" % (self.id,self.name)






# class Musique(db.Model):
# 	id		=db.Column(db.Integer, primary_key=True)
# 	entryId	=db.Column(db.Integer)
# 	releaseYear	=db.Column(db.Integer)
# 	title	=db.Column(db.String(120))
# 	parent	=db.Column(db.String(250))
# 	img		=db.Column(db.String(90))
# 	singer_id =db.Column(db.Integer,db.ForeignKey("singer.id"))
	

# 	singer    = db.relationship("Singer",
# 			backref=db.backref("musiques",lazy="dynamic"))

# 	def __repr__(self):
# 		return "<Musique (%d) %s" %(self.id, self.title)


# class Classification(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	id_musique=db.Column(db.Integer,db.ForeignKey('musique.id'))
# 	id_genre=db.Column(db.Integer,db.ForeignKey('genre.id'))
# 	musique=db.relationship(Musique, backref=db.backref("genre_assoc"))
# 	genre=db.relationship(Genre, backref=db.backref("musique_assoc"))

# class Favoris(db.Model):
# 	id=db.Column(db.Integer, primary_key=True)
# 	id_musique=db.Column(db.Integer,db.ForeignKey('musique.id'))
# 	pseudo=db.Column(db.String(100),db.ForeignKey('user.pseudo'))
# 	musique=db.relationship(Musique, backref=db.backref("musique_assoc"))
# 	user=db.relationship(User,backref=db.backref("User"))

# def get_sample(debut=0,nb=18):
# 	return Musique.query.offset(debut).limit(nb).all()


# def get_genre(title):
# 	s = db.session()
# 	classification=s.query(Classification).join(Musique).join(Genre).filter(Musique.title == title).all()
# 	genre=[]
# 	for c in classification:
# 		genre.append(c.genre.name)
# 	return genre

# def getMusique(pseudo):
# 	s = db.session()
# 	m=s.query(Musique).join(Favoris).filter(Favoris.pseudo==pseudo).all()
# 	musique=[]
# 	for c in m:
# 		musique.append(c)
# 	return musique

# def FavorisOuPas(idM,pseudo):
# 	s = db.session()
# 	m=s.query(Musique).join(Favoris).filter(Favoris.pseudo==pseudo,Musique.id==idM).all()
# 	musique=[]	
# 	for c in m:
# 		musique.append(c)
# 	if len(musique)>0:
# 		return True
# 	else:
# 		 return False

# def removeFavoris(idM,pseudo):
# 	s = db.session()
# 	m=s.query(Favoris).join(Musique).filter(Favoris.pseudo==pseudo,Musique.id==idM).all()
# 	for c in m:
#    		db.session.delete(c)

# def removeMusique(idM):
# 	s = db.session()
# 	m=s.query(Musique).filter(Musique.id==idM).all()
# 	for c in m:
#    		db.session.delete(c)
   		
# def get_books(filtre,debut):
# 	# return Book.query.offset(debut).limit(nb).filter()
# 	pass
# def get_chanteur(id):
# 	return Singer.query.get(id)
	

# def get_chanteurs(debut=0):
# 	return Singer.query.offset(debut).limit(20).all()
	

# def add_chanteur(o):
# 	db.session.add(o)

# def add_favoris(f):
# 	db.session.add(f)

# def getNbrMusiques():
# 	return Musique.query.count()

# def getNbrSinger():
# 	return Singer.query.count()