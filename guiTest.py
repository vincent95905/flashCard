import tkinter as tk


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

		for F in (PagePrincipale, SecondPage):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(PagePrincipale)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	def getApplication(self):
		return self.application


# buttonEntrainement = tk.Button(self, text="Visit page 1", command=lambda: controler.show_frame(SecondPage))

class PagePrincipale(tk.Frame):

	def __init__(self, container, controler):
		tk.Frame.__init__(self, container)
		self.container = container
		self.controler = controler

		messageBienvenue = tk.Label(self, text="Bienvenue sur flashcard")
		buttonEntrainement = tk.Button(self, text="Visit page 1", command=lambda: controler.show_frame(SecondPage))
		buttonAjout = tk.Button(self, text="buttonAjout", command=lambda: self.popupAjoutCarte())
		self.afficherPaquetDansListeBox()

		buttonEntrainement.grid(row=1, column=0)
		messageBienvenue.grid(row=0, column=0)
		buttonAjout.grid(row=3, column=0)

	def getContainer(self):
		return self.container

	def getControler(self):
		return self.controler

	def getApplication(self):
		return self.getControler().getApplication()

	def afficherPaquetDansListeBox(self):
		listbox = tk.Listbox(self)
		listbox.grid(row=2, column=0)

		for item in self.getApplication().getNomTousLesPaquets():
			listbox.insert(tk.END, item)

	def popupAjoutCarte(self):
		top = tk.Toplevel()
		top.title("Ajout d'un paquet")

		indicationUtilisateur = tk.Label(top, text="Nom : ")
		indicationUtilisateur.grid(row=0, column=0)

		saisieUtilisateur = tk.Entry(top)
		saisieUtilisateur.grid(row=0, column=1)

		buttonValider = tk.Button(top, text="Ajouter",
			command=lambda: self.checkEntreUtilisateurAjoutCarte(saisieUtilisateur.get()))
		buttonValider.grid(row=1, column=0)

		buttonQuit = tk.Button(top, text="quit", command=top.destroy)
		buttonQuit.grid(row=1, column=1)

	# Verifie que le paquet a un nom, et qu'il n'existe pas deja dans la liste des paquets (evite les doublons)
	def checkEntreUtilisateurAjoutCarte(self, nomPaquet):
		if(nomPaquet != ""):
			listeNomPaquets = self.getApplication().getNomTousLesPaquets()
			if(nomPaquet not in listeNomPaquets):
				self.getApplication().creerPaquet(nomPaquet)

class SecondPage(tk.Frame):

	def __init__(self, container, controler):
		tk.Frame.__init__(self, container)
		label = tk.Label(self, text="tata")
		label.pack()

# app = Application()
# app.mainloop()