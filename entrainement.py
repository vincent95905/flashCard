

class Entrainement():

	def __init__(self, paquet):
		self.paquetEntrainement = paquet

	def getPaquetEntrainement(self):
		return self.paquetEntrainement

	def setPaquetEntrainement(self, paquetEntrainement):
		self.paquetEntrainement = paquetEntrainement

	def __str__(self):
		s = "le paquet sur lequel on s'entraine est : "
		s += self.getPaquetEntrainement().__str__()

	def commencerEntrainement(self):
		print("on commence l'entrainement")