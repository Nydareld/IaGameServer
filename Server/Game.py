#! /bin/ipython3
import math
import random
import json

gamesize = 10000

class Game:
    """
    Classe qui définit le jeu

    atributs :
        gamesize : taille du plateau (carré)
        joueurs : Un dictionaire des joueurs avec Nom:joueur
                        (Il y a un joueur nommé PNJ qui contient des spheres qui apparaissent aléatoirement)
    """
    def __init__(self, gamesize, nbSpherePnj, nbMaxSpherePnj, minTailleSpheresPnj, maxTailleSpheresPnj):
        self.gamesize = gamesize
        self.nbMaxSpherePnj = nbMaxSpherePnj
        self.minTailleSpheresPnj = minTailleSpheresPnj
        self.maxTailleSpheresPnj = maxTailleSpheresPnj
        self.joueurs = dict()
        self.joueurs["PNJ"] = Player(ia="",username="PNJ",gamesize=gamesize)
        for i in range(nbSpherePnj):
            self.joueurs["PNJ"].spheres.append(
                Sphere(
                    random.randint(1, gamesize),
                    random.randint(1, gamesize),
                    taille=random.randint(minTailleSpheresPnj,maxTailleSpheresPnj)
                )
            )

    def addJoueur(self,player):
        #print(json.dumps(player,default=lambda o: o.__dict__))
        self.joueurs[player.username] = player

    def toJson(self):
        """
        Retrourne le jeu simplifié en Json
        """
        res = dict()
        for joueur in self.joueurs.values():
            res[joueur.username] = []
            for sphere in joueur.spheres:
                res[joueur.username].append([
                    sphere.vectPos,
                    sphere.taille
                    ])
            res[joueur.username]
        return json.dumps(res,default=lambda o: o.__dict__)

    def scoresJson(self):
        res = dict()
        for joueur in self.joueurs.values():
            res[joueur.username] = joueur.score
        return json.dumps(res,default=lambda o: o.__dict__)

class Player:
    """
    Classe qui définit un joueurs

    atributs :
        ia : l'intéligence atrificiel en cours d'utilisation
        spheres : la liste des spheres du joueurs
        username : le nom d'utilisateur du joueur
    """
    def __init__(self,ia,username, gamesize):
        self.username = username
        self.spheres = []
        self.ia = ia
        self.score = 1
        self.poidTotal = 1
        self.end = False
        if username != "PNJ":
            self.spheres.append(
                Sphere(
                    random.randint(1, gamesize),
                    random.randint(1, gamesize),
                    taille=random.randint(10000,100000)))
            self.spheres.append(
                Sphere(
                    random.randint(1, gamesize),
                    random.randint(1, gamesize),
                    random.randint(10000,100000)))
            self.spheres.append(
                Sphere(
                    random.randint(1, gamesize),
                    random.randint(1, gamesize),
                    random.randint(10000,100000)))
            # self.spheres.append(
            #     Sphere(
            #         random.randint(1, gamesize),
            #         random.randint(1, gamesize),
            #         taille=1320))
            # self.spheres.append(
            #     Sphere(
            #         random.randint(1, gamesize),
            #         random.randint(1, gamesize),
            #         taille=1328))
            # self.spheres.append(
            #     Sphere(
            #         random.randint(1, gamesize),
            #         random.randint(1, gamesize),
            #         taille=2225))
            # self.spheres.append(
            #     Sphere(
            #         random.randint(1, gamesize),
            #         random.randint(1, gamesize),
            #         taille=1211))
            # self.spheres.append(
            #     Sphere(
            #         random.randint(1, gamesize),
            #         random.randint(1, gamesize),
            #         taille=2512))
            # self.spheres.append(
            #     Sphere(
            #         random.randint(1, gamesize),
            #         random.randint(1, gamesize),
            #         taille=1230))
            # self.spheres.append(
            #     Sphere(
            #         random.randint(1, gamesize),
            #         random.randint(1, gamesize),
            #         taille=1000))


    def updateScore(self):
        sumtaille = 0
        for sphere in self.spheres:
            sumtaille += sphere.taille
        if sumtaille > self.score:
            self.score = sumtaille


class Sphere:
    """
    Classe qui définit une Sphere

    atributs :
        posX : position en X
        posY : position en Y
        taille : taille de la sphere
        coefitionVitesse : coefitien de vitesse a multiplier avec la vitesse max (en fonction de la taille) pour obtenir la vitesse
        angle : angle vers ou se dirrige la sphere(en degres)
    """
    def __init__(self,posX,posY, taille = 1):
        self.taille = taille
        self.vectVitesse = [0,0]
        self.vectAcceleration = [0,0]
        self.vectPos = [posX,posY]
        #self.t=0

    def getInertie(self):
        return 1/2*taille*vitesse**2

    def posNextTick(self):

        #### Positions accélérées selon le vecteur accélération
        x=self.vectPos[0]+self.vectVitesse[0]+1/2*self.vectAcceleration[0]**2
        y=self.vectPos[1]+self.vectVitesse[1]+1/2*self.vectAcceleration[1]**2

        #### Positions translatées aléatoires
        # x+= random.randint(-100,100)
        # y+= random.randint(-100,100)

        #### Positions translaté de facon circulaires
        #x+=50*math.cos(self.t)#La ca tourne(pour les tests)
        #y+=50*math.sin(self.t)

        #### Modification aléatoire du vecteur accélération
        self.vectAcceleration[0]= random.randint(-3,3)
        self.vectAcceleration[1]= random.randint(-3,3)
        #print("x="+str(int(x))+"y="+str(int(y)))
        #self.t+=1/30

        if x > gamesize :
            x=gamesize
            self.vectVitesse[0]=0
            self.vectAcceleration[0]=0
        if y > gamesize :
            self.vectVitesse[1]=0
            self.vectAcceleration[1]=0
            y=gamesize

        if x < 0 :
            x=0
            self.vectVitesse[0]=0
            self.vectAcceleration[0]=0
        if y < 0 :
            y=0
            self.vectVitesse[1]=0
            self.vectAcceleration[1]=0
        return [int(x),int(y)]

    def vitesseNextTick(self):
        vx=self.vectVitesse[0]+self.vectAcceleration[0]
        vy=self.vectVitesse[1]+self.vectAcceleration[1]
        return [vx,vy]

    def normeVitesse(self):
        return math.sqrt(self.vectVitesse[0]**2 + self.vectVitesse[1]**2 )

    def normeVitesseMax(self):
        return ((1/self.taille)*10000000)+10

    def rayon(self):
        return math.sqrt(self.taille)


    def distanceTo(self,sphere2):
        #print(str(math.sqrt((sphere2.vectPos[0]-self.vectPos[0])**2  + (sphere2.vectPos[1]-self.vectPos[1])**2 )))
        return math.sqrt((sphere2.vectPos[0]-self.vectPos[0])**2  + (sphere2.vectPos[1]-self.vectPos[1])**2 )

    def canJoin(self,sphere2):
        return (
            ( self.distanceTo(sphere2)< self.rayon() ) # la distance entre les 2 centres < la moité du rayon de l'autre
            and                                                           # ET
            (0.8*self.taille > sphere2.taille)                            # la sphere2 fais moins de 80% de la taille de cette sphere ci
            )

    def join(self,sphere2,player2):
        if self.canJoin(sphere2):
            #print("On a mangé, D="+str(self.distanceTo(sphere2))+" ,R="+str(self.rayon()))
            self.taille += (sphere2.taille)*1.5
            return [player2,sphere2]
        return None
