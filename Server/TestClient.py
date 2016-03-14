#! /bin/ipython3

import json
import random
import time
import math
import requests
import threading
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)

ip = "127.0.0.1"
port = 5555

pygame.init()
screen = pygame.display.set_mode((500, 500))

screen.fill(WHITE)
pygame.display.flip()

def affGame(game,screen):
    nbSpheres = 0
    screen.fill([255, 255, 255])
    for joueur in game.values():
        color= (random.randint (0,255),random.randint (0,255),
                            random.randint (0,255))
        for sphere in joueur:
            nbSpheres +=1
            x=sphere[0][0]
            y=sphere[0][1]
            s=sphere[1]
            pygame.draw.circle(screen, color, [int(x/20),int(y/20)], int(math.sqrt(s)/2))
    pygame.display.flip()
    return nbSpheres

def client(ip, port, screen):
    tick = 0
    erreur = 0

    testJoueurs =[
        "/?username=P1&ia=RandIa",
        "/?username=P2&ia=RandIa",
        "/?username=P3&ia=RandIa",
        "/?username=P4&ia=RandIa",
    ]

    url = 'http://'+str(ip)+':'+str(port)

    for joueur in testJoueurs:
        requests.get(url+joueur)

    while True:
        tick +=1
        nb = 0
        try:
            r = requests.get(url).text
            game = json.loads(r)
            nb = affGame(game,screen)
        except:
            print("error "+str(erreur))
            erreur += 1
        if tick % 120 ==0:
            print("Nombre de spheres: "+str(nb))
        time.sleep(1/60)


client(ip,port,screen)
