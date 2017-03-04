import tkinter as tk


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
            print("6 : quitter")

            try:
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
                    continuer = 0
            except ValueError:
                print("Donne moi un nombre saloppe !")
            print("**************************")

    def afficherPaquetCourant(self):
        print(self.getApplication().getPaquetCourant())

    def afficherListePaquet(self):
        i = 0

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
            self.getApplication().setIndexPaquetCourantDansListePaquet(index)
            print("le paquet courant est desormais : {}".format(
                self.getApplication().getListePaquet()[index].getNom()))
        else:
            print("C'est deja le paquet courant")


class InterfaceGraphique(tk.Frame):

    def __init__(self, application):
        self.interface = tk.Tk()
        self.interface.mainloop()
        self.interface.destroy()

        self.interface.minsize(width=400, height=400)
        self.fenetre = tk.Frame.__init__(self, self.interface, width=400, height=400)

        self.application = application
        self.identifiant = ""
        self.valeur = ""
        self.identifiantEntrainement = ""
        self.valeurEntrainement = ""

        self.setButton()
        self.setEntry()

    def getIdentifiantEntrainement(self):
        return self.identifiantEntrainement

    def setIdentifiantEntrainement(self, valeur):
        self.identifiantEntrainement = valeur

    def getValeurEntrainement(self):
        return self.valeurEntrainement

    def setValeurEntrainement(self, valeur):
        self.valeurEntrainement = valeur

    def setEntry(self):
        self.idEntry = tk.Entry()
        self.idEntry.pack()

        self.valeurEntry = tk.Entry()
        self.valeurEntry.pack()

    def setButton(self):
        # self.boutonQuitter = tk.Button(self, text="Quitter", command=self.quit)
        # self.boutonQuitter.pack()

        self.boutonAddCarte = tk.Button(
            self, text="Ajout Carte", command=self.getCarte)
        self.boutonAddCarte.pack()

        self.boutonViderPaquet = tk.Button(
            self, text="Vider Paquet", command=self.viderPaquet)
        self.boutonViderPaquet.pack()

        self.afficherPaquetCourant = tk.Button(
            self, text="Paquet Courant", command=self.affichePaquetCourant)
        self.afficherPaquetCourant.pack()

        self.entrainemenent = tk.Button(
            self, text="entrainemenent", command=self.startTraining)
        self.entrainemenent.pack()

        self.valider = tk.Button(self, text="valider", command=self.valider)
        self.valider.pack()

    def getCarte(self):
        if(self.idEntry.get() != "" and self.valeurEntry.get() != ""):
            self.identifiant = self.idEntry.get()
            self.valeur = self.valeurEntry.get()
            self.application.ajouterCartePaquetCourant(self.identifiant, self.valeur)

        self.idEntry.delete(0, tk.END)
        self.valeurEntry.delete(0, tk.END)

    def viderPaquet(self):
        self.application.viderPaquetCourant()
        print("paquet courant vide")

    def affichePaquetCourant(self):
        self.application.getPaquetCourant()

    def startTraining(self):
        identifiant, valeur = self.application.training()
        # print("id : {}, valeur {}".format(identifiant, valeur))
        self.setIdentifiantEntrainement(identifiant)
        self.setValeurEntrainement(valeur)
        self.idEntry.delete(0, tk.END)
        self.idEntry.insert(0, self.getIdentifiantEntrainement())

    def valider(self):
        result = self.getValeurEntrainement() == self.valeurEntry.get()
        # Si le resultat est bon
        if(result):
            self.valeurEntry.delete(0, tk.END)
            self.idEntry.delete(0, tk.END)
            self.idEntry.insert(0, "Good")
            self.valeurEntry.delete(0, tk.END)
        else:
            self.valeurEntry.delete(0, tk.END)
            self.valeurEntry.insert(0, "Nop")
            self.valeurEntry.delete(0, tk.END)
