#! /bin/ipython3

from http.server import BaseHTTPRequestHandler,HTTPServer
from Server.GameThread import GameThread
from Server.PlayerThread import PlayerThread
import json
import cgi
from urllib.parse import urlparse
from urllib.parse import parse_qs

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    # Get request pour récupérer le jeu a l'instant t
    def do_GET(self):

        if self.path != "/":
            try:
                parsed = urlparse(self.path)
                username = parse_qs(parsed.query)['username'][0]
                ia = parse_qs(parsed.query)['ia'][0]
                #print("username= "+parse_qs(parsed.query)['username'][0])
                #print("Ia= "+parse_qs(parsed.query)['ia'][0])
                print("Nouveau Joueur, Username= "+username+", IA= "+ia)
                #Créer le joueur
                thJoueur = PlayerThread(self.server.gameThread,username,ia)
                thJoueur.start()
            except KeyError:
                pass

        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        # Send the html message
        self.server.gameThread.update()
        data = self.server.gameThread.data
        self.wfile.write(bytes(data,'ascii'))

        return


class GameServer(HTTPServer):

    def __init__(self, server_address, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        HTTPServer.__init__(self, server_address, myHandler)

        self.gameThread = GameThread()
        # self.gameThread.start()
