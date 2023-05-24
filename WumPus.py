import random
import sys
import time
import os

def AffichagePlateau():
    """
    Affiche le plateau de jeu
    """
    print ("     5 ------------ 0")
    print ("    /  \          /  \ ")
    print ("   /    \        /    \ ")
    print ("  /      11-----6      \ ")
    print (" /      /        \      \ ")
    print ("4 ---- 10         7 ---- 1")
    print (" \      \        /      /")
    print ("  \      9------8      / ")
    print ("   \    /        \    /")
    print ("    \  /          \  /")
    print ("     3 ------------ 2")


def PlacementPions(plateau):
    """
    Retourne un plateau aléatoire grâce à la variable 'plateau' 
    """
    random.shuffle(plateau)
    return plateau

def PlacementJoueur(plateau):
    """
    Retourne la position du joueur dans la variable 'player'
    """
    for i in range(len(plateau)):
        if plateau[i]==1:
            player = i
    return player


def PlacementWumPus(plateau,WumPus):
    """
    Retourne la position du Wum Pus avec la variable 'Wum Pus'
    """
    for i in range(len(plateau)):
        if plateau[i] == 2:
            WumPus = i
    return WumPus

def piecesAutour(pieces,Personnage):
    """
    Retourne la liste des pièces autour d'un personnage dans la variable 'pieces'
    """
    i=Personnage
    if i == 11:
        pieces[0]=6
    elif i== 5:
        pieces[0]=0
    else:
        pieces[0]=i+1
    
    if i == 0:
        pieces[1]=5
    elif i == 6:
        pieces[1]=11
    else:
        pieces[1]=i-1

    if i>5: #len liste
        pieces[2]=i-6 #lenliste
    else:
        pieces[2]=i+6
    return pieces

def Message(pieces,plateau):
    """
    Affiche les messages de danger au joueur s'il y en a
    """
    a=0
    for i in pieces:
        if  (plateau[i] == 3 or plateau[i] == 2 or  plateau[i] == 4) and (a==0):
            print ("\nVous entendez:")
            a+=1
        if plateau[i] == 3:
            print ("- Un battement d'aile")
        elif plateau[i] == 2:
            print ("- Le ronflement du Wumpus")
        elif plateau[i] == 4:
            print ("- Un courant d'air")


def AffichageDetail(player,plateau,pieces):
    """
    Affiche plusieurs informations importantes au joueur
    """
    time.sleep(3)
    os.system('clear')
    AffichagePlateau()
    player=PlacementJoueur(plateau)
    print ("\nVous êtes à la position",player)
    Message(piecesAutour(pieces,player),plateau)

def DeplacementWumPus(piecesWP,WumPus,plateau):
    """
    retourne le plateau après déplacement du Wum Pus grâce à la variable 'plateau'
    """
    WumPus=PlacementWumPus(plateau,WumPus)
    piecesWP = piecesAutour(piecesWP,PlacementWumPus(plateau,WumPus))
    compteur=0
    choix=0
    for i in piecesWP:
        if plateau[i] == 3 or plateau[i]== 4:
            compteur+=1
    if compteur ==3:
        while not (plateau[piecesWP[choix]] == 3):
            choix=random.randint(0,2)
        plateau[WumPus]=3
        plateau[piecesWP[choix]]=2    
        return plateau
    while not (plateau[piecesWP[choix]] == 0 or plateau[piecesWP[choix]] == 1):
            choix=random.randint(0,2)
    if plateau[piecesWP[choix]] == 1:
        print ("Perdu, le Wum Pus vous a sauté dessus")
        sys.exit()
    plateau[WumPus]=0
    plateau[piecesWP[choix]]=2
    print ("Le Wum Pus s'est déplacé")
    return plateau


def ChoixDeplacement(player,plateau,pieces):
    """
    Retourne le choix de déplacement du joueur avec la variable 'choix'
    """
    AffichageDetail(player,plateau,pieces)
    print ("\nOù voulez-vous aller?\n","Salles",pieces[0],",",pieces[1],"ou",pieces[2],"?")
    choix=int(input())
    while ( not (choix == pieces[0] or choix == pieces[1] or choix == pieces[2])):
        choix=int(input ("\nLe choix n'est pas bon\n"))
    return choix


def Deplacement(plateau,player,choix):
    """
    retourne le plateau après Déplacement du joueur avec la variable 'plateau'
    """
    os.system('clear')
    while plateau[choix]==3:
        os.system('clear')
        print("Vous croisez le chemin d'une chauve-souris, celle-ci vous teleporte")
        choix=random.randint(0,11)
    if plateau[choix]==2:
        print ("Perdu, vous vous êtes jeté(e) dans la gueule du Wumpus")
        sys.exit()
    elif plateau[choix]==4:
        print ("Perdu, vous êtes tombé(e) dans un puit")
        sys.exit()
    else:
        plateau[player]=plateau[choix]
        plateau[choix]=1
    return plateau


def TirerFleche(player,pieces,fleche,plateau,piecesWP,WumPus):
    """
    retourne le nombre de flèches restantes grâce à la variable 'fleche'
    """
    AffichageDetail(player,plateau,pieces)
    print ("\nDans quelle pièce voulez-vous tirer? (Entre",pieces[0],",",pieces[1],"et",pieces[2],")\n")
    pieceTir=int(input ())
    while not (pieceTir==pieces[0] or pieceTir==pieces[1] or pieceTir==pieces[2]):
        print ("Veuillez entrer une valeur entre",pieces[0],",",pieces[1],"et",pieces[2],")\n")
        pieceTir=int(input())
    if plateau[pieceTir] == 2:
        print ("C'est gagné, le wum pus est mort!")
        sys.exit()
    else:
        fleche-=1
        DeplacementWumPus(piecesWP,WumPus,plateau)
        print ("Loupé, il vous reste", fleche, "flèche(s)")
    return fleche


def ChoixFlechePieces(fleche,plateau,piecesWP,WumPus,pieces,player):
    """
    Retourne le plateau et le nombre de fleches
    """
    print ("\nVoulez-vous:", "\n1: Tirer une flèche?", "\n2: Vous déplacer?")
    choix=''
    while choix.isdigit() == False:
        print ("\nVeuillez entrer 1 ou 2")
        choix=input()
    if int(choix) ==1:
        fleche=TirerFleche(player,pieces,fleche,plateau,piecesWP,WumPus)
        return plateau,fleche
    elif int(choix) == 2:
        plateau=Deplacement(plateau,player,ChoixDeplacement(player,plateau,piecesAutour(pieces,player)))
        return plateau,fleche
    else:
        print ("Veuillez entrer 1 ou 2")



def Game():
    """
    Organisation du jeu
    """
    #Initialisation
    plateau=[0,0,0,0,0,0,1,2,3,3,4,4]
    player=0
    WumPus=0
    fleche=3
    pieces=[0,0,0]
    piecesWP=[0,0,0]
    plateau=PlacementPions(plateau)
    player=PlacementJoueur(plateau)

    #Début jeu
    while fleche>=1:
        AffichageDetail(player,plateau,pieces)    
        plateau,fleche=ChoixFlechePieces(fleche, plateau, piecesWP, WumPus, pieces,player)
    print ("Perdu, vous n'avez plus de flèche")

if __name__=="__main__":
    Game()