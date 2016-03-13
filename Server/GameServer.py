#! /bin/ipython3

from http.server import BaseHTTPRequestHandler,HTTPServer
from GameLoop import GameLoop
import json


#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    # Get request pour récupérer le jeu a l'instant t
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        # Send the html message
        data = "zbra"
        self.wfile.write(bytes(json.dumps(data,default=lambda o: o.__dict__),'ascii'))
        return

    # Handler for the POST requests
    # Post request en cas de nouveau joueur
    def do_POST(self):
        return


class GameServer(HTTPServer):

    def __init__(self, server_address, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        HTTPServer.__init__(self, server_address, myHandler)

        self.GameLoop = GameLoop()
