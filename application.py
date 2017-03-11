import pickle
#import tkinter as tk
import os
import random
from objets import *
from interface import *
from entrainement import *
from constantes import *

#############################
# Class Application
# Constitue la classe la plus haute dans la hierarchie de l'application
#############################


class Application:

    def __init__(self):
        self.nom = "Application"
        self.listePaquet = self.chargerListePaquetSauvegarde()
        self.nombrePaquet = 0
        # Retourne l'index du paquet sur lequel on travail
        self.indexPaquetCourantDansListePaquet = self.initPaquetCourant()
        self.interface = InterfaceConsole(self)
        #self.interface = InterfaceGrahique(self)

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getListePaquet(self):
        return self.listePaquet

    def setListePaquet(self, listePaquet):
        self.listePaquet = listePaquet

    def getNombrePaquet(self):
        return self.nombrePaquet

    def setNombrePaquet(self, nombrePaquet):
        self.nombrePaquet = nombrePaquet

    def getIndexPaquetCourantDansListePaquet(self):
        return self.indexPaquetCourantDansListePaquet

    def setIndexPaquetCourantDansListePaquet(self, index):
        if(index >= len(self.getListePaquet())):
            print("index non valide")
        else:
            self.indexPaquetCourantDansListePaquet = index

    def getPaquetCourant(self):
        return self.getListePaquet()[self.getIndexPaquetCourantDansListePaquet()]

    def chargerListePaquetSauvegarde(self):
        liste = []
        chemin = "paquets/"

        listeFichiers = os.listdir(chemin)
        nombrePaquet = len(listeFichiers)
        print(
            "liste fichier present dans le repertoire paquets/ : {}".format(listeFichiers))

        if(nombrePaquet == 0):
            print("pas de sauvegarde, on va en cree une")
            paquet = Paquet("paquetParDefaut", "paquets/")
            liste.append(paquet)
            # self.sauvegarderPaquet(paquet)
        else:
            for paquet in listeFichiers:
                cheminDeChaquePaquet = chemin + paquet
                with open(cheminDeChaquePaquet, 'rb') as handle:
                    paquet = pickle.load(handle)
                    liste.append(paquet)

        self.setNombrePaquet(len(liste))
        return liste

    # Initialise l'index du paquet courant
    # On parcourt la liste de paquet et si il il a la variable getIsPaquetCourant a true, on renvoie l'index qu'il a
    def initPaquetCourant(self):
        # Si pas de paquet dans la liste
        if(len(self.getListePaquet()) == 0):
            return 0
        else:
            i = 0
            for paquet in self.getListePaquet():
                if(paquet.getIsPaquetCourant()):
                    return i
                i += 1

    # On change le paquet courant avec l'index d'un autre paquet et on sauvegarde les deux paquets modifies
    def changementPaquetCourant(self, indexNouveauPaquetCourant):
        self.getPaquetCourant().setIsPaquetCourant(False)
        self.sauvegarderPaquet(self.getPaquetCourant())

        # print("ancien paquet courant {}".format(self.getPaquetCourant().getNom()))

        self.setIndexPaquetCourantDansListePaquet(indexNouveauPaquetCourant)
        self.getPaquetCourant().setIsPaquetCourant(True)
        
        # print("nouveau paquet courant {}".format(self.getPaquetCourant().getNom()))

        self.sauvegarderPaquet(self.getPaquetCourant())

    # Creer un paquet et l'ajoute a la liste de paquet en fournissant juste le
    # nom du paquet
    def creerPaquet(self, nomPaquet):
        paquet = Paquet(nomPaquet, "paquets/")
        self.ajouterPaquetListePaquet(paquet)

    def ajouterPaquetListePaquet(self, paquet):
        self.getListePaquet().append(paquet)
        self.setNombrePaquet(self.getNombrePaquet() + 1)
        self.sauvegarderPaquet(paquet)

    # Recuperer Carte depuis interface et l'ajoute au paquetCourant
    def ajouterCartePaquetCourant(self, identifiant, valeur):
        c = Carte(identifiant, valeur)
        self.getPaquetCourant().ajoutCarte(c)
        self.sauvegarderPaquet(self.getPaquetCourant())

    def sauvegarderPaquet(self, paquet):
        chemin = paquet.getChemin() + paquet.getNom()
        print("chemin : {}".format(paquet.getChemin()))
        with open(chemin, 'wb') as output:
            pickle._dump(paquet, output, pickle.HIGHEST_PROTOCOL)

        print("sauvegarde a {}".format(chemin))

    def chargementPaquet(self, nomPaquetACharger):
        chemin = "paquets/" + nomPaquetACharger
        with open(chemin, 'rb') as handle:
            self.getListePaquet()[self.getIndexPaquetCourantDansListePaquet()] = pickle.load(handle)
        

    def viderPaquetCourant(self):
        # i = self.getPaquetCourant().getNombreCarte() - 1
        # print("i : {}".format(i))
        # print("-----")
        # while(i >= 0):
        #     # print(len(self.getPaquetCourant().getListeCarte()))
        #     del self.getPaquetCourant().getListeCarte()[i]
        #     i -= 1

        self.getPaquetCourant().viderPaquet()
        self.setNombrePaquet(len(self.getListePaquet()))
        self.getPaquetCourant().setNombreCarte(0)
        self.sauvegarderPaquet(self.getPaquetCourant())

    # C'est la qu'on va appeler la classe entrainement et on fou le bordel relatif a l'entrainement la bas
    def startEntrainement(self):
        entrainement = Entrainement(self.getPaquetCourant(), self)
        entrainement.gestionEntrainement()
        self.chargementPaquet(self.getPaquetCourant().getNom())
        print("fin entrainement")
        # self.sauvegarderPaquet(self.getPaquetCourant())

def main():
    Application()


main()
