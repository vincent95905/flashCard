
class Carte:

    def __init__(self, identifiant, valeur):
        self.identifiant = identifiant
        self.valeur = valeur

    def getIdentifiant(self):
        return self.identifiant

    def setIdentifiant(self, identifiant):
        self.identifiant = identifiant

    def getValeur(self):
        return self.valeur

    def setValeur(self, valeur):
        self.valeur = valeur

    def __str__(self):
        s = self.identifiant
        s += " | "
        s += self.valeur
        return s

    def modifierCarte(self, identifiant, valeur):
        self.setIdentifiant(identifiant)
        self.setValeur(valeur)


class Paquet:

    def __init__(self, nom, chemin):
        self.listeCarte = []
        self.nom = nom
        self.chemin = chemin
        self.nombreCarte = 0

    def __getitem__(self, index):
        return self.getListeCarte()[index]

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