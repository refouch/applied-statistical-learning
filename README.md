# Projet d'apprentissage statistique appliqué

Projet de classification de titres musicaux selon leur genre réalisé par Lucas Cumunel et Rémi Foucherand.
Nous utilisons le jeu de données Free Music Archive (ou FMA) disponible ici: "https://os.unil.cloud.switch.ch/fma/fma_metadata.zip"

## Comment reproduire les résultats ?

### Étape 1: Télécharger le datset et les librairires.
Cela se fait automatiquement à l'aide d'un script que nous avons écrit. En se plaçant à la racine du projet, écrire simplement dans un terminal:
```bash:
python3 setup.py
```
Cela va démarrer automatiquement le téléchargement du jeu de données et des librairies python nécéssaires.
Il suffit ensuite de sélectionner le bon environnement virtuel (nommé env) lors de la lecture de chaque notebook.

**Dans le cas où le script ne fonctionnerait pas**, les données peuvent être téléchargées manuellement et placées dans un dossier ```data/fma_metadata```.
On peut aussi créer un environnement virtuel contenant toutes les dépendances nécéssaires en exécutant les trois commandes suivantes:
```bash:
python3 -m venv env
```
```bash:
source env/bin/activate
```
```bash:
pip install -r requirements.txt
```

### Étape 2: Reproduction des résultats

Pour reproduire nos résultats et comprendre notre démarche, il convient d'exécuter les fichiers dans l'ordre suivant : 

- logreg.ipynb (régression logistique)
- neural_net.ipynb (réseau de neurones)
- convnet.ipynb (réseau de neurones convolutionnel)
- rf.ipynb (forêt aléatoire)
- XGboost.ipynb (algorithme XGBoost)

Chaque notebook Jupyter correspond à un modèle différent appliqué au même jeu de données contenant des *features* Librosa agrégées des titres du Free Music Archives (FMA).