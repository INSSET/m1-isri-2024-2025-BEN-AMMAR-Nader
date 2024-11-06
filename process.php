<?php

// Vérifier si les données sont envoyées via POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les valeurs du formulaire
    $nom = isset($_POST['nom']) ? $_POST['nom'] : '';
    $prenom = isset($_POST['prenom']) ? $_POST['prenom'] : '';

    // Vérification de la présence des données
    if (!empty($nom) && !empty($prenom)) {
        // Créer un tableau associatif avec les données
        $utilisateur = [
            'nom' => $nom,
            'prenom' => $prenom
        ];

        // Lire le contenu actuel du fichier JSON (si existant)
        $fichier = 'utilisateurs.json';
        if (file_exists($fichier)) {
            $json_data = file_get_contents($fichier);
            $utilisateurs = json_decode($json_data, true);
        } else {
            $utilisateurs = [];
        }

        // Ajouter le nouvel utilisateur au tableau
        $utilisateurs[] = $utilisateur;

        // Sauvegarder le tableau dans le fichier JSON
        file_put_contents($fichier, json_encode($utilisateurs, JSON_PRETTY_PRINT));

        // Afficher les données envoyées à l'utilisateur
        echo "<h1>Données reçues</h1>";
        echo "<p><strong>Nom :</strong> " . htmlspecialchars($nom) . "</p>";
        echo "<p><strong>Prénom :</strong> " . htmlspecialchars($prenom) . "</p>";
        echo "<p>Les informations ont été enregistrées dans le fichier <code>utilisateurs.json</code>.</p>";
    } else {
        echo "<p>Les champs nom et prénom sont requis.</p>";
    }
}
