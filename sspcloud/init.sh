#!/bin/bash
set -e  # stoppe le script si une commande échoue

# ===== Variables =====
WORK_DIR="/home/onyxia/work"
REPO_URL="https://github.com/refouch/applied-statistical-learning.git"
REPO_NAME="applied-statistical-learning"
CLONE_DIR="${WORK_DIR}/${REPO_NAME}"

echo "🚀 Initialisation de l'environnement SSP Cloud..."
echo "📂 Dossier de travail : ${WORK_DIR}"

# ===== Clonage du dépôt =====
echo "📦 Clonage du dépôt GitHub..."
git clone "${REPO_URL}" "${CLONE_DIR}"

# ===== Installation éventuelle d’extensions utiles =====
code-server --install-extension ms-python.python
code-server --install-extension quarto.quarto

# ===== Ouverture du dossier dans VS Code =====
echo "🧭 Ouverture du projet dans VS Code..."
code-server --reuse-window "${CLONE_DIR}"

echo "✅ Environnement prêt. Bon travail !"
