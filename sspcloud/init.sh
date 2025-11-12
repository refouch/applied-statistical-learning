#!/bin/bash
# ===========================================
# Script d'initialisation SSP Cloud
# Projet : applied-statistical-learning
# Auteur : Rémi Fouchérand
# ===========================================

# --- 1. Préparation de l'environnement de travail ---
echo "=== Initialisation de l'environnement SSP Cloud ==="

# Aller dans le répertoire de travail (habituel sur SSP Cloud)
cd "${HOME}" || exit

# --- 2. Cloner ton dépôt GitHub ---
echo "=== Clonage du dépôt GitHub ==="
if [ ! -d "applied-statistical-learning" ]; then
    git clone https://github.com/refouch/applied-statistical-learning.git
else
    echo "Le dépôt existe déjà, mise à jour..."
    cd applied-statistical-learning || exit
    git pull
    cd ..
fi

cd applied-statistical-learning || exit

MAIN_NOTEBOOK="main.ipynb"

if [ -f "$MAIN_NOTEBOOK" ]; then
    echo "=== Ouverture du notebook principal : $MAIN_NOTEBOOK ==="
    code "$MAIN_NOTEBOOK"
else
    echo "Notebook principal introuvable. Ouvre le manuellement depuis VS Code."
fi

echo "=== Initialisation terminée ==="
