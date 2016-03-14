from Game import *
from threading import Thread


class PlayerThread(Thread):

    def __init__(self, GameThread, username, ia):
        self.GameThread = GameThread
        self.username = username
        self.barrierEtape._parties = self.barrierTours._parties
        self.ia = ia

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

    def executeIa():
        pass

    def calculePos():
        pass

    def join():
        pass
