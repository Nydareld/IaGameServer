#! /bin/ipython3

from Server.GameServer import GameServer


PORT= 5555

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = GameServer(('', PORT))
    print('Started httpserver on port '+str(PORT))

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
