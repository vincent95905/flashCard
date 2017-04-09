import tkinter as tk
from entrainement import *

# Classe qui fait office de controler pour l'interface graphique
# Lie la classe application avec l'interface graphique
class ApplicationGraphique(tk.Tk):

	def __init__(self, application):
		tk.Tk.__init__(self)
		self.application = application
		container = tk.Frame(self, width=500, height=500)

		container.grid()
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (PagePrincipale, PageEntrainement):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(PagePrincipale)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.refreshPage()
		frame.tkraise()

	def getApplication(self):
		return self.application


# buttonEntrainement = tk.Button(self, text="Visit page 1", command=lambda: controler.show_frame(SecondPage))

class PagePrincipale(tk.Frame):

	def __init__(self, container, controler):
		tk.Frame.__init__(self, container)
		self.container = container
		self.controler = controler

		# Represente le paquet selectionne dans la listebox. Permet de savoir quel paquet nous allons utilise
		self.paquetSelectionne = ""

		self.creationWidget()
		self.dispositionWidget()
		self.bindWidget()
		
		self.afficherPaquetDansListeBox()

		
	def creationWidget(self):
		self.listbox = tk.Listbox(self)

		self.messageBienvenue = tk.Label(self, text="Bienvenue sur flashcard")
		self.nomPaquetCourant = tk.Label(self, text=self.getApplication().getNomPaquetCourant())
		
		self.buttonEntrainement = tk.Button(self, text="Entrainement", command=lambda: self.controler.show_frame(PageEntrainement))
		self.buttonAjoutPaquet = tk.Button(self, text="Ajout d'un paquet", command=lambda: self.creerPopupAjoutPaquet())
		self.buttonAjoutCarte = tk.Button(self, text="Ajout une carte", command=lambda: self.creerPopupAjoutCarte())

		self.buttonTest = tk.Button(self, text="test")

	def dispositionWidget(self):
		self.listbox.grid(row=2, column=0)
		self.buttonEntrainement.grid(row=2, column=1)
		self.messageBienvenue.grid(row=0, column=0)
		self.nomPaquetCourant.grid(row=1, column=0)
		self.buttonAjoutPaquet.grid(row=3, column=0)
		self.buttonTest.grid(row=4, column=0)
		self.buttonAjoutCarte.grid(row=1, column=1)

	def bindWidget(self):
		self.listbox.bind("<Double-Button-1>", lambda var: self.getNomPaquetSelectionneDansListeBox())

	def getContainer(self):
		return self.container

	def getControler(self):
		return self.controler

	def getApplication(self):
		return self.getControler().getApplication()

	# Permet de recuperer le nom du paquet sur lequel l'utilisateur est dans la listebox
	# et de mettre a jour le paquet courant sur ce paquet
	def getNomPaquetSelectionneDansListeBox(self):
		tuple = self.listbox.curselection()
		# print(self.listbox.curselection())

		self.paquetSelectionne = self.listbox.get(tuple)

		# On met a jour le paquet courant en fonction du paquet choisi par l'utilisateur dans la listebox
		self.controler.getApplication().setIndexPaquetCourantDepuisNomPaquet(self.paquetSelectionne)
		self.nomPaquetCourant.configure(text=self.getApplication().getNomPaquetCourant())


	# Fonction appele a chaque fois qu'on raise la page
	# Permet de rafraichir les contenus, et tkWidget
	def refreshPage(self):
		print("refresh de la PagePrincipale")

	# Supprime l'ensemble des elements de la listebox et affiche tous les noms de paquet
	def afficherPaquetDansListeBox(self):
		self.listbox.delete(0, tk.END)
		for item in self.getApplication().getNomTousLesPaquets():
			self.listbox.insert(tk.END, item)

	def creerPopupAjoutPaquet(self):
		popupAjoutPaquet(self)

	def creerPopupAjoutCarte(self):
		popupAjoutCarte(self)


class popupAjoutCarte(tk.Toplevel):

	def __init__(self, pageParent):

		tk.Toplevel.__init__(self)
		self.pageParent = pageParent

		self.creationWidget()
		self.dispositionWidget()
		
		

	def creationWidget(self):
		self.identifiant = tk.Label(self, text="identifiant")
		self.valeur = tk.Label(self, text="valeur")

		self.identifiantEntry = tk.Entry(self)
		self.valeurEntry = tk.Entry(self)

		self.valideButton = tk.Button(self, text="Valider", command= lambda: self.checkEntreUtilisateurAjoutCarte())

		self.buttonQuit = tk.Button(self, text="quit", command=self.destroy)

	def dispositionWidget(self):
		self.buttonQuit.grid(row=3, column=1)
		self.identifiant.grid(row=1, column=0)
		self.valeur.grid(row=2, column=0)
		self.identifiantEntry.grid(row=1, column=1)
		self.valeurEntry.grid(row=2, column=1)
		self.valideButton.grid(row=3, column=0)

	def getApplication(self):
		return self.pageParent.getApplication()

	def checkEntreUtilisateurAjoutCarte(self):
		identifiant = self.identifiantEntry.get()
		valeur = self.valeurEntry.get()

		print("identifiant {}, valeur {}".format(identifiant, valeur))

		# Si l'utilisateur a saisi quelque chose
		if(identifiant != "" and valeur != ""):
			listeIdentifiant = self.getApplication().getIdentifiantCartesPaquetCourant()
			if(identifiant not in listeIdentifiant):
				self.getApplication().ajouterCartePaquetCourant(identifiant, valeur)




class popupAjoutPaquet(tk.Toplevel):
	def __init__(self, pageParent):
		tk.Toplevel.__init__(self)
		self.pageParent = pageParent

		self.creationWidget()
		self.dispositionWidget()
		
		

	def creationWidget(self):
		self.indicationUtilisateur = tk.Label(self, text="Nom : ")
		self.saisieUtilisateur = tk.Entry(self)
		self.infoAjoutPaquet = tk.Label(self, text=" ")
		self.buttonValider = tk.Button(self, text="Ajouter", 
			command=lambda: self.checkEntreUtilisateurAjoutPaquet(self.saisieUtilisateur.get()))
		self.buttonQuit = tk.Button(self, text="quit", command=self.destroy)

	def dispositionWidget(self):
		self.indicationUtilisateur.grid(row=0, column=0)
		self.saisieUtilisateur.grid(row=0, column=1)	
		self.infoAjoutPaquet.grid(row=1, column=0)
		self.buttonValider.grid(row=2, column=0)
		self.buttonQuit.grid(row=2, column=1)

	def getApplication(self):
		return self.pageParent.getApplication()

		# Verifie que le paquet a un nom, et qu'il n'existe pas deja dans la liste des paquets (evite les doublons)
	def checkEntreUtilisateurAjoutPaquet(self, nomPaquet):
		if(nomPaquet != ""):
			listeNomPaquets = self.getApplication().getNomTousLesPaquets()
			if(nomPaquet not in listeNomPaquets):
				self.getApplication().creerPaquet(nomPaquet)
				self.pageParent.afficherPaquetDansListeBox()
				self.infoAjoutPaquet['text'] = "Paquet enregistree"
			else:
				self.infoAjoutPaquet['text'] = "Le paquet existe deja"
		else:
			self.infoAjoutPaquet['text'] = "paquet vide non autorise"


class PageEntrainement(tk.Frame):

	def __init__(self, container, controler):
		tk.Frame.__init__(self, container)

		self.container = container
		self.controler = controler

		self.creationWidget()
		self.dispositionWidget()		

		# self.getApplication().creerEntrainement()

	def getApplication(self):
		return self.controler.getApplication()


	def creationWidget(self):
		self.titre = tk.Label(self, text="")
		self.buttonMenuPrincipale = tk.Button(self, text="Menu Principal", command=lambda: self.controler.show_frame(PagePrincipale))
		self.infoPaquet = tk.Label(self, text="")
		
		self.identifiant = tk.Label(self, text="identifiant")
		self.valeur = tk.Label(self, text="valeur")

		self.boutonFacile = tk.Button(self, text="Facile")
		self.boutonMoyen = tk.Button(self, text="Moyen")
		self.boutonDifficile = tk.Button(self, text="Difficile")

	def dispositionWidget(self):
		self.titre.grid(row=0, column=2)
		self.buttonMenuPrincipale.grid(row=2, column=1)
		self.infoPaquet.grid(row=1, column=0)
		self.identifiant.grid(row=4, column=1)
		self.valeur.grid(row=5, column=1)
		self.boutonFacile.grid(row=6, column=0)
		self.boutonMoyen.grid(row=6, column=1)
		self.boutonDifficile.grid(row=6, column=3)

	# Fonction appele a chaque fois qu'on raise la page
	# Permet de rafraichir les contenus, et tkWidget
	def refreshPage(self):
		# Refresh le titre du paquet courant
		self.titre.configure(text=self.getApplication().getNomPaquetCourant())

		# Refresh les informations du paquet courant
		self.infoPaquet.configure(text=self.getApplication().getPaquetCourant().__str__())

# app = Application()
# app.mainloop()