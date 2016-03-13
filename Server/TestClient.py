#! /bin/ipython3

import json
import time
import requests
import threading
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)

ip = "127.0.0.1"
port = 8080

pygame.init()
screen = pygame.display.set_mode((500, 500))

screen.fill(WHITE)
pygame.display.flip()

def affGame(game,screen):
    screen.fill([255, 255, 255])
    for joueur in game.values():
        color= (random.randint (0,255),random.randint (0,255),
                            random.randint (0,255))
        for sphere in joueur:
            x=sphere[0][0]
            y=sphere[0][1]
            s=sphere[1]
            pygame.draw.circle(screen, color, [int(x/20),int(y/20)], int(math.sqrt(s)/2))
    pygame.display.flip()


def client(ip, port, screen):
    tick = 0
    erreur = 0

    jsonHeaders = {'content-type': 'application/json'}

    #player=input("Username ?:")
    player = "Nyda"
    data = dict()
    data["Username"]=player
    data["Ia"]="rand"

    url = 'http://'+str(ip)+':'+str(port)

    rep = requests.post(url, data=json.dumps(data,default=lambda o: o.__dict__), headers=jsonHeaders)

    while True:
        tick +=1
        try:
            pass
            #game = json.loads(requests.get(url))
            #affGame(game,screen)
        except json.JSONDecodeError:
            erreur += 1
        time.sleep(1000/30)


client(ip,port,screen)
