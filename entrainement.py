from constantes import *
from random import randrange
import sys
import time

class Entrainement():

	def __init__(self, paquet, application):
		self.paquetEntrainement = paquet
		self.application = application

		self.listeCarteDifficulteFacile = self.triCarte()[1]
		self.listeCarteDifficulteNonDefini = self.triCarte()[0]
		self.listeCarteDifficulteMoyenne = self.triCarte()[2]
		self.listeCarteDifficulteDifficile = self.triCarte()[3]
		self.carteTireAuSort = self.tireAuSortCarte()

	def getCarteTireAuSort(self):
		return self.carteTireAuSort

	def setCarteTireAuSort(self, carte):
		self.carteTireAuSort = carte

	def getPaquetEntrainement(self):
		return self.paquetEntrainement

	def setPaquetEntrainement(self, paquetEntrainement):
		self.paquetEntrainement = paquetEntrainement

	def getListeFacile(self):
		return self.listeCarteDifficulteFacile

	def setListeFacile(self, listeFacile):
		self.listeCarteDifficulteFacile = listeFacile

	def getListeNonDefini(self):
		return self.listeCarteDifficulteNonDefini

	def setListeNonDefini(self, listeNonDefini):
		self.listeCarteDifficulteNonDefini = listeNonDefini

	def getListeMoyen(self):
		return self.listeCarteDifficulteMoyenne

	def setListeMoyen(self, listeMoyen):
		self.listeCarteDifficulteMoyenne = listeMoyen

	def getListeDifficile(self):
		return self.listeCarteDifficulteDifficile

	def setListeDifficile(self, listeDifficile):
		self.listeCarteDifficulteDifficile = listeDifficile

	def getApplication(self):
		return self.application

	def setApplication(self, application):
		self.application = application

	def afficheListe(self, liste):
		for item in liste:
			print(item)

	def __str__(self):
		s = "le paquet sur lequel on s'entraine est : "
		s += self.getPaquetEntrainement().getNom()

	def changeCarteTireAuSort(self):
		self.carteTireAuSort = self.tireAuSortCarte()

	# Tri les cartes en fonction de leur difficulte dans 4 listes
	# Permet de faire le tri qu'une seule fois
	def triCarte(self):
		listeFacile = []
		listeMoyen = []
		listeDifficile = []
		listeNonDefini = []

		for carte in self.getPaquetEntrainement():
			if(carte.getDifficulte() == NON_DEFINI):
				listeNonDefini.append(carte)
			elif(carte.getDifficulte() == FACILE):
				listeFacile.append(carte)
			elif(carte.getDifficulte() == MOYEN):
				listeMoyen.append(carte)
			elif(carte.getDifficulte() == DIFFICILE):
				listeDifficile.append(carte)

		return listeNonDefini, listeFacile, listeMoyen, listeDifficile

	# Tire au sort une carte parmis les listes de paquet
	def tireAuSortCarte(self):

		if(self.getPaquetEntrainement().getNombreCarte() > 0):
			# Tant qu'il y a des cartes dans la liste des non définies, on les affiche
			if(len(self.getListeNonDefini()) != 0):
				carte =  self.getListeNonDefini()[0]
				del self.listeCarteDifficulteNonDefini[0]
				return carte

			# 2 fois plus de chance de tomber sur une moyenne que facile
			# 4 fois plus de chance de tomber sur une difficile que moyenne
			else:
				carteNonTrouve = 1
				while(carteNonTrouve):
					print("toto")
					print("len liste facile : ", len(self.getListeFacile()))
					print("len liste moyen : ", len(self.getListeMoyen()))
					print("len liste difficile : ", len(self.getListeDifficile()))
					nombreAleatoire = randrange(1, 22)
					# print("nombre aleatoire : {}".format(nombreAleatoire))
					if(nombreAleatoire <= 2 and len(self.getListeFacile()) != 0):
						print("1")
						# Tire dans la liste facile
						indexCarteAleatoire = randrange(0, len(self.getListeFacile()))
						carte = self.getListeFacile()[indexCarteAleatoire]
						# carte.setDifficulte(FACILE)
						del self.getListeFacile()[indexCarteAleatoire]
						carteNonTrouve = 0
						return carte 

					elif(nombreAleatoire >= 3 and nombreAleatoire <= 6 and len(self.getListeMoyen()) != 0):
						print("2")
						# Tire dans la liste moyen
						indexCarteAleatoire = randrange(0, len(self.getListeMoyen()))
						carte = self.getListeMoyen()[indexCarteAleatoire]
						# carte.setDifficulte(MOYEN)
						del self.getListeMoyen()[indexCarteAleatoire]
						carteNonTrouve = 0
						return carte

					elif(nombreAleatoire >= 7 and len(self.getListeDifficile()) != 0):
						print("3")
						# Tire dans la liste difficile
						indexCarteAleatoire = randrange(0, len(self.getListeDifficile()))
						carte = self.getListeDifficile()[indexCarteAleatoire]
						# carte.setDifficulte(DIFFICILE)
						del self.getListeDifficile()[indexCarteAleatoire]
						carteNonTrouve = 0
						return carte 
					if(len(self.getListeFacile()) == 0 and len(self.getListeMoyen()) == 0 and len(self.getListeDifficile()) == 0):
						print("liste de difficulte vide")
						break
		else:
			print("Paquet d'entrainement vide")

	# Supprime le paquet d'entrainement, et le rempli avec les cartes dont la difficulte a ete modifie
	# Puis on sauvegarde le paquet
	def reformerPaquetAvecCartesTrieEtDifficulte(self):
		self.getPaquetEntrainement().viderPaquet()

		for carte in self.getListeNonDefini():
			self.getPaquetEntrainement().ajoutCarte(carte)

		for carte in self.getListeFacile():
			self.getPaquetEntrainement().ajoutCarte(carte)

		for carte in self.getListeMoyen():
			self.getPaquetEntrainement().ajoutCarte(carte)

		for carte in self.getListeDifficile():
			self.getPaquetEntrainement().ajoutCarte(carte)
		
		print("paquet non defini")
		self.afficheListe(self.getListeNonDefini())
		print("-----------")
		print("paquet facile")
		self.afficheListe(self.getListeFacile())
		print("-----------")
		print("paquet moyen")
		self.afficheListe(self.getListeMoyen())
		print("-----------")
		print("paquet difficile")
		self.afficheListe(self.getListeDifficile())
		print("-----------")

		# print("paquet entrainement")
		# # self.afficheListe(self.getPaquetEntrainement())
		# print(self.getPaquetEntrainement())
		
		self.getPaquetEntrainement().sauvegarde()

	def gestionEntrainement(self, entreeUtilisateur):

		# Si il y au moins une carte dans le paquet d'entrainement
		if(self.getPaquetEntrainement().getNombreCarte() > 0):

			if(entreeUtilisateur == FACILE):
				self.getCarteTireAuSort().setDifficulte(FACILE)
				self.getListeFacile().append(self.getCarteTireAuSort())
				self.reformerPaquetAvecCartesTrieEtDifficulte()
			elif(entreeUtilisateur == MOYEN):
				self.getCarteTireAuSort().setDifficulte(MOYEN)
				self.getListeMoyen().append(self.getCarteTireAuSort())
				self.reformerPaquetAvecCartesTrieEtDifficulte()
			elif(entreeUtilisateur == DIFFICILE):
				self.getCarteTireAuSort().setDifficulte(DIFFICILE)
				self.getListeDifficile().append(self.getCarteTireAuSort())
				self.reformerPaquetAvecCartesTrieEtDifficulte()
				# elif(choix == "a"):
				#	print("nomber carte paquet entrainement : {}".format(self.getPaquetEntrainement().getNombreCarte()))

			self.setCarteTireAuSort(self.tireAuSortCarte())
			self.getApplication().chargementPaquet(self.getApplication().getPaquetCourant().getNom())
		else:
			print("Impossible de s'entrainer sur un paquet vide")
