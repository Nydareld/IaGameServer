
from .app import app, db, ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from flask import url_for,redirect,render_template
from werkzeug import secure_filename
# from .models import get_sample, get_chanteur,get_chanteurs,add_chanteur,get_genre,getNbrMusiques,getNbrSinger,add_favoris,getMusique,FavorisOuPas,removeFavoris,removeMusique
from flask.ext.login import login_user, current_user, logout_user
from flask import request
from flask.ext.wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from wtforms import PasswordField
from .models import User, Ia, removeIa, getUser, removeUser
from hashlib import sha256
import os
import requests
import Server
import time
import random
from threading import Thread


# from .models import Musique,Singer

						####### home #######

@app.route("/")
def home():

	return  render_template(
			"home.html",
			title="CodIA",
			tab="Accueil"
			)



@app.route("/classement")
def classement():
	return  render_template(
			"classement.html",
			title="Classement",
			users=User.query.all(),
			tab="Classement"
			)

@app.route("/reglement")
def reglement():
	return render_template("reglement.html",tab="Règles")

@app.route("/myprofil/", methods=("GET","POST",))
def MyProfil(pseudo="joseph"):
	if request.method=="GET":
		return render_template("profile.html", tab="MyProfil")
	else:
		u=getUser(request.form["pseudo"])
		u.pseudo=request.form["pseudo"]
		u.username=request.form["username"]
		u.usersurname=request.form["usersurname"]
		u.useremail=request.form["useremail"]
		m = sha256()
		m.update((request.form["password"]).encode())
		u.password = m.hexdigest()
		db.session.add(u)
		db.session.commit()
	return render_template("profile.html", tab="MyProfil")

@app.route("/MesIA")
def MesIA():
	return render_template("/MesIA.html",ia=Ia.query.all(),tab="MesIA")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/addIA', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            i=Ia()
            i.user_pseudo=current_user.pseudo
            i.name=filename
            db.session.add(i)
            db.session.commit()
            return redirect(url_for('MesIA'))

    return render_template("addIA.html",tab="MesIA")


@app.route("/suprIa/<string:filename>")
def suprIa(filename):
		os.remove(app.config['UPLOAD_FOLDER']+filename)
		removeIa(filename)
		db.session.commit()
		return redirect(url_for('MesIA'))


@app.route("/administrer")
def administrer():
	return  render_template(
			"administrer.html",
			title="Administrer",
			tab="administrer",
			users=User.query.all(),
			ia=Ia.query.all())

@app.route("/suprUser/<string:pseudo>")
def suprUser(pseudo):
	removeUser(pseudo)
	db.session.commit()
	return  render_template(
			"administrer.html",
			title="Administrer",
			tab="administrer",
			users=User.query.all())

@app.route("/modifIa/<string:filename>")
def modifIa(filename):
	fichier = (open("CodIa/tuto/IA/"+filename, "r")).read()
	return  render_template(
			"modif.html",
			title="Modif",
			tab="MesIA",
			file=filename,
			fic=fichier
			)

@app.route('/save_file/<string:filename>', methods=['POST'])
def save_file(filename):
	contenu = request.form['textarea']
	newFichier = open("CodIa/tuto/IA/"+filename,"w")
	newFichier.write(contenu)
	newFichier.close()
	return redirect(url_for("MesIA"))



#quand nous cliquons sur une image spécifique

# @app.route("/one_music/<int:id>/")
# def one_music(id):
# 	return  render_template(
# 			"one_music.html",
# 			music=Musique.query.get(id),
# 			genres=get_genre(Musique.query.get(id).title),
# 			fav=FavorisOuPas)


#paggination + recherche par titre du musique
# @app.route("/img/")
# @app.route("/img/<int:debut>/")
# @app.route("/img/<string:filter>/")
# @app.route("/<string:filter>/")
# @app.route("/img/<int:debut>/<int:nb>")
# @app.route("/img/<int:debut>/<int:nb>/<string:filter>/")

# def image(debut=0,nb=19, filter=None):
# 	if filter != None:
# 		musiques=Musique.query.filter(Musique.title.contains(filter)).all()
# 	else:
# 		musiques=get_sample(debut,nb)
# 	return render_template(
# 			"home.html",
# 			debut=debut,
# 			nb=nb,
# 			title="Tiny Amazon",
# 			musiques=musiques)


				########## Chanteurs ############
# class ChanteurForm(Form):
# 	id = HiddenField('id')
# 	name = StringField('Nom', validators=[DataRequired()])

# # list des chanteurs
# @app.route("/Chanteur")
# @app.route("/nb/<int:deb>")
# def Chanteur(deb=0):
# 	return  render_template(
# 			"Chanteur.html",
# 			title="Chanteurs",
# 			deb=deb,
# 			nb=18,
# 			Chanteurs=get_chanteurs(deb),
# 			nbrchanteurs=getNbrSinger()
# 			)




# @app.route("/edit/chanteur/<int:id>")
# def edit_chanteur(id):
# 	if(id!=0):
# 		a=get_chanteur(id)
# 		f=ChanteurForm(id=a.id, name=a.name)
# 	else:
# 		a=None
# 		f=ChanteurForm()
# 	return render_template(
# 		"edit_chanteur.html",
# 		chanteur=a , form=f)





# @app.route("/save/chanteur/", methods=("POST",))
# def save_chanteur():
# 	a=None
# 	f=ChanteurForm()
# 	if(f.validate_on_submit()):
# 		id = int(f.id.data)
# 		a= get_chanteur(id)
# 		a.name = f.name.data
# 		db.session.commit()
# 		return redirect(url_for('edit_chanteur', id=a.id))

# 	a= get_chanteur(int(f.id.data))
# 	return render_template(
# 		"edit_chanteur.html",
# 		chanteur=a, form=f)


# @app.route("/ajoute/chanteur/", methods=("POST",))
# def ajouter_chanteur():
# 	a=Singer(name=None)
# 	f=ChanteurForm()

# 	if(f.validate_on_submit()):
# 		id = Singer.query.count()+1
# 		a.id = id
# 		a.name = f.name.data
# 		add_chanteur(a)
# 		db.session.commit()
# 		return redirect(url_for('edit_chanteur', id=a.id))
# 	a= get_chanteur(int(f.id.data))
# 	return render_template(
# 		"edit_chanteur.html",
# 		chanteur=a, form=f)


					########### Login/Logiut ############

class UserForm(Form) :
	mail = StringField('ADRESSE MAIL', validators=[DataRequired()])
	pseudo = StringField('PSEUDO', validators=[DataRequired()])
	name = StringField('NOM', validators=[DataRequired()])
	prenom = StringField('PRENOM', validators=[DataRequired()])
	mdp = PasswordField('MOT DE PASSE', validators=[DataRequired()])

	def get_user(pseudo):
		return User.get(pseudo)



@app.route("/ajout/")
def ajout_client():
	f=UserForm(name=None, prenom=None, mail=None, mdp=None)
	return render_template("ajout-client.html", form=f,tab="Inscription")


from hashlib import sha256
from flask.ext.login import login_user, current_user
@app.route("/ajouter/client/", methods=("POST",))
def ajouter_client():
	a = None
	f = UserForm()
	if User.query.get(f.pseudo.data)!=None:
		msg = "Votre pseudo est deja pris, merci de le changer. Faites travailler votre imagination !"
		return render_template(
			"ajout-client.html",
			form=f,
			message=msg)
	if f.validate_on_submit():
		u = User() #Creation du nouvelle instance
		#Ses parametres
		u.pseudo = f.pseudo.data
		u.usermail = f.mail.data
		u.username = f.name.data
		u.usersurname = f.prenom.data
		u.score=0
		m = sha256()
		m.update((f.mdp.data).encode())
		u.password = m.hexdigest()
		#u.usercode = User.query.count()+1
		login_user(u) #je le connecte
		db.session.add(u)
		db.session.commit()
		return render_template('bienvenue.html',nom=u.username)
	msg = "Un probleme dans vos saisies. Un petit effort, recommencez !"
	return render_template(
		"ajout-client.html",
		form=f,
		message=msg)

@app.route("/bienvenue")
def bienvenue(name):
	return render_template("bienvenue.html",nom=name)

from .models import User

class LoginForm(Form):
	pseudo = StringField("Nom d'utilisateur (pseudo)")
	password = PasswordField('Mot de passe')
	next = HiddenField()

	def get_authenticated_user(self):
		user = User.query.get(self.pseudo.data)
		if user is None :
			return None
		m = sha256()
		m.update(self.password.data.encode())
		passwd = m.hexdigest()
		return user if passwd == user.password else None




from flask import request

@app.route("/login/", methods=("GET","POST",))
def login():
	f = LoginForm()
	if not f.is_submitted() :
		f.next.data = request.args.get("next")
	elif f.validate_on_submit():
		inscrit = f.get_authenticated_user()
		if inscrit is not None :
			login_user(inscrit)
			next = f.next.data or url_for("home")
			return redirect(next)
	return render_template(
		"login.html",
		form = f,tab="Connexion")

@app.route("/logout/")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/data")
def data():
	return app.gameThread.data

@app.route("/scores")
def scores():
	return app.gameThread.scores

@app.route("/addPlayer/<string:username>/<string:ia>")
def addPlayer(username, ia):
	print("Nouveau Joueur sur le serveur par defaut, Username= "+username+", IA= "+ia)
	#Créer le joueur
	thJoueur = Server.PlayerThread(app.gameThread,username,ia)
	thJoueur.start()
	return redirect(url_for("home"))

@app.route("/randTestPlayers")
def randTestPlayers():
	def createLesJoueurs():
		joueurs = ["Nico","Clem","Flavie","theo","Marine","aifpe"]
		for n in joueurs:
			rand = random.random()
			time.sleep(rand*3)
			thJoueur = Server.PlayerThread(app.gameThread,n,"Rand")
			thJoueur.start()

	th = Thread(target=createLesJoueurs)
	th.start()
	return redirect(url_for("home"))


						########Contact######


@app.route("/apropos")
def apropos():
	return render_template("apropos.html",tab="Apropos")


					####Musique Favoris#####



# @app.route("/ajouterFavoris/<int:idM>+<string:idU>")
# def ajouterFavoris(idM,idU):
# 	f=Favoris(id_musique=None, pseudo=None)
# 	# f.id=Favoris.query.count()+1
# 	# id = Favoris.query.count()+1
# 	# f.id=id
# 	f.id_musique=idM
# 	f.pseudo=idU
# 	add_favoris(f)
# 	db.session.commit()
# 	return redirect(url_for('one_music', id=idM))

# @app.route("/Musique")
# def MesMusiques():
# 	return render_template("musique.html",musiques=getMusique)

# @app.route("/SuprimerFavoris/<int:idM>+<string:idU>")
# def suprFav(idM,idU):
# 	removeFavoris(idM,idU)
# 	db.session.commit()
# 	return redirect(url_for('one_music', id=idM))

# 				####Musique####

# @app.route("/suprimerMusique/<int:idM>")
# def suprMusique(idM):
# 	removeMusique(idM)
# 	db.session.commit()
# 	return redirect(url_for('home'))

# class MusiqueForm(Form) :
# 	mail = StringField('ADRESSE MAIL', validators=[DataRequired()])
# 	pseudo = StringField('PSEUDO', validators=[DataRequired()])
# 	name = StringField('NOM', validators=[DataRequired()])
# 	prenom = StringField('PRENOM', validators=[DataRequired()])
# 	mdp = PasswordField('MOT DE PASSE', validators=[DataRequired()])
