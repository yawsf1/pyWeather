# Application Météo (Python + Tkinter)

Ce projet est une application de bureau développée en Python avec Tkinter.  
Elle permet d'afficher en temps réel les données météorologiques d'une ville donnée.  
L'utilisateur peut saisir le nom de n'importe quelle ville et obtenir :

- la température en degrés Celsius  
- le taux d'humidité  
- la vitesse du vent  
- la condition météorologique générale (ensoleillé, nuageux, etc.)

L'application utilise la bibliothèque `requests` pour interroger une API météo (comme OpenWeatherMap).  
Les données sont récupérées au format JSON, puis affichées dans une interface simple et intuitive réalisée avec Tkinter.

Pour exécuter cette application, vous devez avoir Python 3 installé.  
Vous devez également installer la bibliothèque `requests` :


pip install requests


Ensuite, récupérez une clé API gratuite sur le site officiel OpenWeatherMap.
Dans le fichier main.py, remplacez YOUR_API_KEY par votre propre clé.

Pour lancer l'application, utilisez la commande suivante :

python weather.py
Exemple d'affichage pour la ville de Paris :

Ville : Paris
Température : 22°C
Humidité : 55%
Vitesse du vent : 3.2 m/s
Condition : Nuageux


Ce projet est un bon point de départ pour apprendre à utiliser des API, manipuler des données JSON, et créer des interfaces graphiques simples en Python.

Licence : MIT

Auteur : Youssef LAAYADI — yawsf1 GitHub
