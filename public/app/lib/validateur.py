import re

class Validateur:
    @staticmethod
    def valider_longueur(valeur):
        """
        Vérifie si la longueur est comprise entre 2 et 60 caractères.
        """
        return 2 <= len(valeur) <= 60

    @staticmethod
    def valider_caracteres(valeur):
        """
        Vérifie si la chaîne contient uniquement des lettres, '-' et espaces.
        """
        return bool(re.match(r"^[a-zA-Z\- ]+$", valeur))

    @staticmethod
    def valider_separateurs(valeur):
        """
        Vérifie que le total des occurrences de '-' et espace ne dépasse pas 5.
        """
        total_separateurs = valeur.count('-') + valeur.count(' ')
        return total_separateurs <= 5


    
    @staticmethod
    def valider_debut_fin(valeur):
        """
        Vérifie que la chaîne ne commence ni ne se termine par '-' ou espace.
        """
        return not (valeur[0] in "- " or valeur[-1] in "- ")

    @staticmethod
    def valider_nom_prenom(valeur):
        """
        Combine toutes les validations.
        """
        return (
            Validateur.valider_longueur(valeur)
            and Validateur.valider_caracteres(valeur)
            and Validateur.valider_separateurs(valeur)  
            and Validateur.valider_debut_fin(valeur)
        )
