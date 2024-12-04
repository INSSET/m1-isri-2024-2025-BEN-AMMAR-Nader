import os

class FichierVisiteur:
    FICHIER = "visiteurs.txt"

    @staticmethod
    def ajout(nom, prenom):
        with open(FichierVisiteur.FICHIER, "a") as fichier:
            fichier.write(f"{nom},{prenom}\n")

    @staticmethod
    def tout_lire():
        if not os.path.exists(FichierVisiteur.FICHIER):
            return []
        with open(FichierVisiteur.FICHIER, "r") as fichier:
            return [ligne.strip() for ligne in fichier.readlines()]
