from .app import manager,db

import Server

@manager.command
def loaddb(filename):
	"""Creates the table and populates them with data."""
	#Création de toutes les tables
	db.create_all()

	# import yaml

	# musiques =yaml.load(open(filename))
	# from .models import Singer, Musique ,Genre,Classification


	# singer ={}
	# for b in musiques:
	# 	a= b["by"]
	# 	if a not in singer:
	# 		o = Singer(name=a)
	# 		db.session.add(o)
	# 		singer[a] = o


	# genres={}
	# for b in musiques:

	# 	for genre in b["genre"]:
	# 		a=genre
	# 		if(a not in genres):
	# 			o=Genre(name=genre)
	# 			db.session.add(o)
	# 			genres[a] = o

	# db.session.commit()


	# musiq={}
	# for b in musiques:
	# 	a = singer[b["by"]]
	# 	o = Musique(entryId   = b["entryId"],
	# 			 releaseYear   = b["releaseYear"],
	# 			 title	 = b["title"],
	# 			 parent	 =b["parent"],
	# 			 img	 =b["img"],
	# 			 singer_id= a.id )
	# 	musiq[b["entryId"]]=o
	# 	db.session.add(o)


	# db.session.commit()





	# for b in musiques:
	# 	musique=musiq[b["entryId"]]
	# 	for genre in b["genre"]:
	# 		g=genres[genre]
	# 		o=Classification(id_musique=musique.id,id_genre=g.id)
	# 		db.session.add(o)
	# db.session.commit()







		# for n in b["genre"]:
		# 	o = Genre(name = n,musique_id=o.id)
		# 	db.session.add(o)




@manager.command
def syncdb():
	'''Creates all missing tables '''
	db.create_all()

@manager.command
def newuser(usermail, username, usersurname, password):
	''' Adds a new user '''
	from .models import User
	from hashlib import sha256
	m = sha256()
	m.update(password.encode())
	u = User(username=username, usersurname=usersurname, usermail=usermail, password=m.hexdigest())
	db.session.add(u)
	db.session.commit()

@manager.command
def runGameServer(port=5555):
	'''Creates and run a game server without web server '''
	port = int(port)
	try:
		server = Server.GameServer(("",port))
		print('Started httpserver on port '+str(port))
		server.serve_forever()

	except KeyboardInterrupt:
	    print('^C received, shutting down the web server')
	    server.socket.close()
