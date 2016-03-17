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
        GameThread.joueursAAdd.append(self.joueur)

        GameThread.nbth += 1


    def run(self):
        while True:
            #attend le début du tours
            # print("Barriere debut de tours "+str(threading.current_thread().name))
            # print(self.GameThread.barrierTours.parties)
            self.GameThread.barrierTours.wait()
            #execute le code de l'IA
            self.executeIa()


            #print(self.GameThread.barrierEtape.parties)
            self.GameThread.barrierEtape.wait()

            self.calculePos()

            self.GameThread.barrierEtape.wait()

            agraille = self.join()

            #print("avant acquire")
            self.GameThread.barrierEtape.wait()
            self.GameThread.lockmanger.acquire()
            self.GameThread.aManger.append(agraille)
            #print("pendant")
            self.GameThread.lockmanger.release()
            #print("après release")
            self.GameThread.barrierManger.wait()
            # time.sleep(1/60)


    def executeIa(self):
        pass

    def calculePos(self):
        # print("\033[91m caca \033[0m")
        # print(str(self.joueur.spheres[0].normeVitesse()) +"    "+ str(self.joueur.spheres[0].normeVitesseMax()))
        for sphere in  self.joueur.spheres:
            sphere.vectVitesse = sphere.vitesseNextTick()
            if sphere.normeVitesse() > sphere.normeVitesseMax():
                # print("\033[91m caca \033[0m")
                sphere.vectVitesse[0] *= 0.9
                sphere.vectVitesse[1] *= 0.9
            # else :
            #     print("\033[92m non caca \033[0m")
            sphere.vectPos = sphere.posNextTick()

        self.joueur.updateScore() 

    def join(self):
        try:
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
        except RuntimeError:
             print("\033[91m Nb de Thread :"+str(self.GameThread.barrierManger._parties)+", "+str(self.GameThread.nbth)+" \033[0m")

        return listjoueur
