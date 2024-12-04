from app.lib.validateur import Validateur
from app.lib.fichier_visiteur import FichierVisiteur

def main():
    print("Bienvenue dans le formulaire de validation !")
    
    while True:
        nom = input("Entrez votre nom : ").strip()
        prenom = input("Entrez votre prénom : ").strip()
        
        if not Validateur.valider_nom_prenom(nom):
            print("Nom invalide. Le nom doit contenir uniquement des lettres, '-' ou espaces, être entre 2 et 60 caractères, et ne pas commencer/terminer par '-' ou espace.")
            continue
        
        if not Validateur.valider_nom_prenom(prenom):
            print("Prénom invalide. Le prénom doit contenir uniquement des lettres, '-' ou espaces, être entre 2 et 60 caractères, et ne pas commencer/terminer par '-' ou espace.")
            continue
        
        # Ajout des informations au fichier
        FichierVisiteur.ajout(nom, prenom)
        print("Données enregistrées avec succès !")
        
        # Affichage des visiteurs enregistrés
        print("\nListe des visiteurs enregistrés :")
        visiteurs = FichierVisiteur.tout_lire()
        for visiteur in visiteurs:
            print(f" - {visiteur}")
        
        # Option pour continuer ou quitter
        continuer = input("\nVoulez-vous ajouter un autre visiteur ? (o/n) : ").strip().lower()
        if continuer != 'o':
            print("Merci d'avoir utilisé notre application. À bientôt !")
            break

if __name__ == "__main__":
    main()
