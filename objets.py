
class Carte:

    def __init__(self, identifiant, valeur):
        self.identifiant = identifiant
        self.valeur = valeur
        self.difficulte = 0 # 0 : facile, 1 : moyen, 2 : difficile, 3 : a revoir

    def getIdentifiant(self):
        return self.identifiant

    def setIdentifiant(self, identifiant):
        self.identifiant = identifiant

    def getValeur(self):
        return self.valeur

    def setValeur(self, valeur):
        self.valeur = valeur

    def getDifficulte(self):
        return self.difficulte

    def setDifficulte(self, difficulte):
        if(difficulte >= 0 and difficulte <= 4):
            self.difficulte = difficulte
        else:
            print("la difficulte doit etre comprise entre 0 et 4 inclu")

    def affichageDifficulte(self):
        if(self.getDifficulte() == 0):
            return "facile"
        elif(self.getDifficulte() == 1):
            return "moyen"
        elif(self.getDifficulte() == 2):
            return "difficile"
        elif(self.getDifficulte() == 3):
            "a revoir"

    def __str__(self):
        s = self.identifiant
        s += " | "
        s += self.valeur
        s += " | "
        s += self.affichageDifficulte()
        return s

    def modifierCarte(self, identifiant, valeur):
        self.setIdentifiant(identifiant)
        self.setValeur(valeur)


class Paquet:

    isPaquetCourantAlreadySet = False

    def __init__(self, nom, chemin):
        self.listeCarte = []
        self.nom = nom
        self.chemin = chemin
        self.nombreCarte = 0
        self.isPaquetCourant = self.managePaquetCourant()

    def __getitem__(self, index):
        return self.getListeCarte()[index]

    # Gere le fait qu'il ne peut exister qu'un seul paquet courant
    def managePaquetCourant(self):
        if(Paquet.isPaquetCourantAlreadySet):
            return False
        else:
            Paquet.isPaquetCourantAlreadySet = True
            return True

    def getIsPaquetCourant(self):
        return self.isPaquetCourant

    def setIsPaquetCourant(self, boolean):
        self.isPaquetCourant = boolean

    def getListeCarte(self):
        return self.listeCarte

    def setListeCarte(self, listeCarte):
        self.listeCarte = listeCarte

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getChemin(self):
        return self.chemin

    def setChemin(self, chemin):
        self.chemin = chemin

    def getNombreCarte(self):
        return self.nombreCarte

    def setNombreCarte(self, nombreCarte):
        self.nombreCarte = nombreCarte

    def ajoutCarte(self, carte):
        self.listeCarte.append(carte)
        self.setNombreCarte(self.getNombreCarte() + 1)

    def __str__(self):
        s = "nom paquet : " + self.getNom()
        s += " | chemin paquet : "
        s += self.getChemin()
        s += " | nombre carte dans le paquet : "
        s += str(self.getNombreCarte())
        s += " | "
        s += str(self.getIsPaquetCourant())
        s += "\n"
        for carte in self.getListeCarte():
            s += carte.__str__()
            s += "\n"
        return s

    def afficheCarte(self):
        s = ""
        for carte in self.getListeCarte():
            s += carte.__str__()
            s += "\n"
        print(s)

    def supprimerCarte(self, carte):
        self.getListeCarte().remove(carte)

        if(self.getNombreCarte() > 0):
            self.setNombreCarte(self.getNombreCarte() - 1)
