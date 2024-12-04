import pytest
import os
from app.lib.fichier_visiteur import FichierVisiteur

@pytest.fixture
def setup_teardown():
    # Setup
    if os.path.exists(FichierVisiteur.FICHIER):
        os.remove(FichierVisiteur.FICHIER)
    yield
    # Teardown
    if os.path.exists(FichierVisiteur.FICHIER):
        os.remove(FichierVisiteur.FICHIER)

def test_ajout_et_tout_lire(setup_teardown):
    FichierVisiteur.ajout("John", "Doe")
    FichierVisiteur.ajout("Jane", "Smith")
    lignes = FichierVisiteur.tout_lire()
    assert lignes == ["John,Doe", "Jane,Smith"]
