from Game import *
from threading import Thread


class PlayerThread(Thread):

    def __init__(self, GameThread, username, ia):
        Thread.__init__(self)
        self.GameThread = GameThread
        self.username = username
        GameThread.barrierEtape._parties = GameThread.barrierTours._parties
        self.ia = ia
        #GameThread.game.joueurs[username]=Player(ia,username,GameThread.game.gamesize)
        GameThread.game.addJoueur(Player(ia,username,GameThread.game.gamesize))


    def run(self):
        while True:
            #attend le début du tours
            self.GameThread.barrierTours.wait()

            #execute le code de l'IA
            self.executeIa()

            self.GameThread.barrierEtape.wait()

            self.calculePos()

            self.GameThread.barrierEtape.wait()

            self.join()

    def executeIa(self):
        pass

    def calculePos(self):
        pass

    def join(self):
        pass
