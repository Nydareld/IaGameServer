from Game import *
from threading import Thread


class PlayerThread(Thread):

    def __init__(self, GameThread, username, ia):
        self.GameThread = GameThread
        self.username = username
        self.ia = ia

    
