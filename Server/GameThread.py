#! /bin/ipython3

from Server.Game import *
from Server.PlayerThread import PlayerThread
from threading import Thread
from threading import Barrier
from threading import Lock

class GameThread(Thread):

    #initialisation du serveur
    def __init__(self, gamesize = 10000, nbSpherePnj=100, nbMaxSpherePnj=1000, minTailleSpheresPnj=1, maxTailleSpheresPnj=3):
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

        self.aManger = []

        self.nbth = 0

        #B2 barriere d'étape
        self.barrierEtape = Barrier(0)
        #B1 barriere de tours
        self.barrierManger = Barrier(0,action=self.manger)
        #barriere de spheres a manger
        self.barrierTours = Barrier(0,action=self.updateNbTh)

    def updateNbTh(self):
        self.data = self.game.toJson()
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
        res = 0
        for boule in self.game.joueurs.keys():
            for x in boule:
                res+=1
        #print(res)

        for dico in self.aManger:
            for joueur in dico:
                for sphere in dico[joueur]:
                    print(self.game.joueurs[joueur])
                    self.game.joueurs[joueur].spheres.remove(sphere)
                    res-=1

        print(res)
        self.aManger = []


    def run(self):
        while True:
            #attendre le temps d'un tick

            #si il y a un nouveau joueur on lajoute et on augmente la barriere

            #execute le code de l'ia

            #calcule les pos

            #ajoute des spheres PNJ

            #Join les bouboules
            pass
