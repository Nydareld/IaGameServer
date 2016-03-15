from Server.Game import *
from threading import Thread
import threading
import time


class PlayerThread(Thread):

    def __init__(self, GameThread, username, ia):
        Thread.__init__(self)
        self.GameThread = GameThread
        self.username = username
        GameThread.barrierTours._parties += 1
        self.ia = ia
        self.joueur = Player(ia,username,GameThread.game.gamesize)
        #GameThread.game.joueurs[username]=Player(ia,username,GameThread.game.gamesize)
        GameThread.game.addJoueur(self.joueur)

        GameThread.nbth += 1


    def run(self):
        while True:
            #attend le début du tours
            #print("Barriere debut de tours "+str(threading.current_thread().name))
            #print(self.GameThread.barrierTours.parties)
            self.GameThread.barrierTours.wait()
            #execute le code de l'IA
            self.executeIa()


            #print(self.GameThread.barrierEtape.parties)
            self.GameThread.barrierEtape.wait()

            self.calculePos()

            self.GameThread.barrierEtape.wait()

            agraille = self.join()
            #print("avant acquire")
            self.GameThread.lockmanger.acquire()
            self.GameThread.aManger.append(agraille)
            #print("pendant")
            self.GameThread.lockmanger.release()
            #print("après release")
            self.GameThread.barrierManger.wait()
            time.sleep(1/60)


    def executeIa(self):
        pass

    def calculePos(self):
        for sphere in  self.joueur.spheres:
            sphere.vectPos = sphere.posNextTick()
        pass

    def join(self):
        listjoueur = dict()
        for sphere in  self.joueur.spheres:
            for joueur2 in self.GameThread.game.joueurs.values():
                for sphere2 in joueur2.spheres:
                    res = sphere.join(sphere2,joueur2)
                    if(res != None):
                        # if(not (listjoueur[res[0].username] in locals)):
                        #     listjoueur[res[0].username] = []
                        try:
                            listjoueur[res[0].username].append(res[1])
                        except KeyError:
                            listjoueur[res[0].username] = []
                            listjoueur[res[0].username].append(res[1])
        return listjoueur
