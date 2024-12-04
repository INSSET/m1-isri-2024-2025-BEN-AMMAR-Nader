import pytest
from app.lib.validateur import Validateur

# Tests pour la longueur
def test_valider_longueur():
    assert Validateur.valider_longueur("John") is True
    assert Validateur.valider_longueur("A" * 60) is True
    assert Validateur.valider_longueur("J") is False  # Trop court
    assert Validateur.valider_longueur("A" * 61) is False  # Trop long

# Tests pour les caractères
def test_valider_caracteres():
    assert Validateur.valider_caracteres("John") is True
    assert Validateur.valider_caracteres("Jean-Pierre") is True
    assert Validateur.valider_caracteres("Anna Maria") is True
    assert Validateur.valider_caracteres("1234") is False  # Contient des chiffres
    assert Validateur.valider_caracteres("Marie@") is False  # Contient '@'

def test_valider_separateurs():
    # Cas valides
    assert Validateur.valider_separateurs("Jean-Pierre") is True
    assert Validateur.valider_separateurs("Jean Piere") is True
    assert Validateur.valider_separateurs("Jean- Pierre") is True  # Total de 2
    assert Validateur.valider_separateurs("Jean - Pierre") is True  # Total de 3

    # Cas invalides
    assert Validateur.valider_separateurs("Jean------Doe") is False  # Trop de '-'
    assert Validateur.valider_separateurs("Jean      Doe") is False  # Trop d'espaces
    assert Validateur.valider_separateurs("Jean-- ---Doe") is False  # Total combiné de 6


# Tests pour début/fin
def test_valider_debut_fin():
    assert Validateur.valider_debut_fin("John") is True
    assert Validateur.valider_debut_fin("-John") is False  # Commence par '-'
    assert Validateur.valider_debut_fin("John-") is False  # Se termine par '-'
    assert Validateur.valider_debut_fin(" John") is False  # Commence par espace
    assert Validateur.valider_debut_fin("John ") is False  # Se termine par espace

# Tests pour la validation complète
def test_valider_nom_prenom():
    assert Validateur.valider_nom_prenom("Jean-Pierre") is True
    assert Validateur.valider_nom_prenom("Anna Maria") is True
    assert Validateur.valider_nom_prenom("1234") is False
    assert Validateur.valider_nom_prenom("Jean------Doe") is False
    assert Validateur.valider_nom_prenom(" John") is False
    assert Validateur.valider_nom_prenom("A" * 61) is False
