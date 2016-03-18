#! /bin/ipython3

from Server.Game import *
from Server.PlayerThread import PlayerThread
from threading import Thread
from threading import Barrier
from threading import Lock
from Server.Game import Sphere
import time


class GameThread():

    #initialisation du serveur
    def __init__(self, gamesize = 10000, nbSpherePnj=100, nbMaxSpherePnj=1000, minTailleSpheresPnj=100, maxTailleSpheresPnj=1000):
        """
        gamesize                Taille du jeu en unités metriques (la carte est carrée)
        nbSpherePnj             nombre de spheres qu'a le PNJ au début
        nbMaxSpherePnj          nombre maximum de spheres qu'a le PNJ
        minTailleSpheresPnj     taille minimum d'une Sphere du PNJ
        maxTailleSpheresPnj     taille maximum d'une Sphere du PNJ
        """
        self.lockmanger = Lock()
        Thread.__init__(self)
        self.game = Game(gamesize, nbSpherePnj, nbMaxSpherePnj, minTailleSpheresPnj, maxTailleSpheresPnj)

        self.data = self.game.toJson()
        self.scores = self.game.scoresJson()


        self.aManger = []

        self.nbth = 0

        self.joueursAAdd = []

        #B2 barriere d'étape
        self.barrierEtape = Barrier(0,action=self.randomPnj)
        #B1 barriere de tours
        self.barrierManger = Barrier(0,action=self.manger)
        #barriere de spheres a manger
        self.barrierTours = Barrier(0,action=self.updateNbTh)

        self.debutTours = time.time()

    def randomPnj(self):
        if len(self.game.joueurs["PNJ"].spheres) < self.game.nbMaxSpherePnj:
            self.game.joueurs["PNJ"].spheres.append(
            Sphere(random.randint(1, gamesize),
            random.randint(1, gamesize),
            taille=random.randint(self.game.minTailleSpheresPnj,self.game.maxTailleSpheresPnj)
        )
    )

    def updateNbTh(self):
        for joueur in self.joueursAAdd:
            self.game.addJoueur(joueur)
        self.joueursAAdd = []
        self.data = self.game.toJson()
        self.scores = self.game.scoresJson()
        self.barrierManger._parties = self.nbth
        self.barrierEtape._parties = self.nbth


    def update(self):
        self.data = self.game.toJson()

    def connect(self, username, ia):
        #incr la barriere barrierTours
        self.barrierTours._parties+=1
        #Créer un threadJoueur
        p = PlayerThread(self, username, ia)
        p.start()


    def manger(self):
        tempsTour = time.time()-self.debutTours
        if(tempsTour < 1/60):
            # print("temps du tour :"+str(tempsTour))
            time.sleep(1/60-tempsTour)
        self.debutTours = time.time()
        #res = 0
        #for boule in self.game.joueurs.keys():
            #for x in boule:
                #res+=1
        #print(res)

        for dico in self.aManger:
            for joueur in dico:
                for sphere in dico[joueur]:
                    # print(self.game.joueurs[joueur])
                    try :
                        self.game.joueurs[joueur].spheres.remove(sphere)
                    except:
                        pass
                        #res-=1

        #print(res)
        self.aManger = []
