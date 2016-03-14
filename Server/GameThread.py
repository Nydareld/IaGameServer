#! /bin/ipython3

from Game import *
from threading import Thread
from threading import Barrier

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
        Thread.__init__(self)
        self.game = Game(gamesize, nbSpherePnj, nbMaxSpherePnj, minTailleSpheresPnj, maxTailleSpheresPnj)
        self.data = self.game.toJson()

        #B1 barriere de tours
        self.barrierTours = Barrier(1,action=updateEtape())
        #B2 barriere d'étape
        self.barrierEtape = Barrier(1)


    def updateEtape(self):
        self.barrierEtape._parties = self.barrierTours._parties

    def connect(self, username, ia):
        #incr la barriere barrierTours
        self.barrierTours+=1
        #Créer un threadJoueur
        

    def run(self):
        while True:
            #attendre le temps d'un tick

            #si il y a un nouveau joueur on lajoute et on augmente la barriere

            #execute le code de l'ia

            #calcule les pos

            #ajoute des spheres PNJ

            #Join les bouboules


            pass
