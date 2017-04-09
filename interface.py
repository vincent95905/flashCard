import tkinter as tk
import sys

class InterfaceConsole():

    def __init__(self, application):
        print("**** Interface console ****")
        self.application = application
        self.mainMenu()

    def getApplication(self):
        return self.application

    def setApplication(self, application):
        self.application = application

    def mainMenu(self):
        continuer = 1
        while(continuer):
            print("**************************")
            print("Que souhaitez vous faire ?")
            print("1 : creer une carte")
            print("2 : creer un paquet")
            print("3 : afficher le paquet courant")
            print("4 : afficher liste des paquets")
            print("5 : changer le paquet courant")
            print("6 : commencer l'entrainement")
            print("7 : quitter")

            try:
                # sys.stdout.flush()
                choix = int(input("Votre choix : "))

                if(choix == 1):
                    self.creerCarte()
                elif(choix == 2):
                    self.creerPaquet()
                elif(choix == 3):
                    self.afficherPaquetCourant()
                elif(choix == 4):
                    self.afficherListePaquet()
                elif(choix == 5):
                    self.changePaquetCourant()
                elif(choix == 6):
                    self.getApplication().startEntrainement()
                elif(choix == 7):
                    continuer = 0
                # elif(choix == 0):
                #     self.getApplication().getNomTousLesPaquets()
            except ValueError:
                print("Donne moi un nombre saloppe !")
            print("**************************")

    def afficherPaquetCourant(self):
        print(self.getApplication().getPaquetCourant())

    def afficherListePaquet(self):
        i = 0
        print("Il y a {} paquets".format(self.getApplication().getNombrePaquet()))
        for paquet in self.getApplication().getListePaquet():
            if(self.getApplication().getIndexPaquetCourantDansListePaquet() == i):
                print("[{}] : {}  => Paquet courant".format(i, paquet.getNom()))
            else:
                print("[{}] : {}".format(i, paquet.getNom()))
            i += 1

    def creerCarte(self):
        print("Saississez un identifiant")
        identifiant = str(input("identifiant : "))
        print("Saisissez une valeur")
        valeur = str(input("valeur : "))

        self.getApplication().ajouterCartePaquetCourant(identifiant, valeur)

    def creerPaquet(self):
        print("Quel est le nom du paquet que vous souhaitez creer ?")
        nomPaquet = str(input("Nom : "))

        self.getApplication().creerPaquet(nomPaquet)

    def changePaquetCourant(self):
        self.afficherListePaquet()
        print("saisissez le nombre du paquet sur lequel vous souhaitez travailler")
        index = int(input("nombre : "))
        if(index != self.getApplication().getIndexPaquetCourantDansListePaquet()):
            self.getApplication().changementPaquetCourant(index)
            print("le paquet courant est desormais : {}".format(
                self.getApplication().getListePaquet()[index].getNom()))
        else:
            print("C'est deja le paquet courant")
