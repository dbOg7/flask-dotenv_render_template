# flask-dotenv_render_template

# Objectif du projet:

- installer un environnement virtuel pour le développement grace a python-dotenv

- installer une application flask avec un template et afficher la page Home

# Installer un environnement virtuel
# Windows

py -m pip install virtualenv

py -m virtualenv venv

.\venv\Scripts\activate

# Linux

pip install virtualenv 

virtualenv venv

source venv/bin/activate

# Installation des modules

pip install -r requirements.txt

# Configurer python-dotenv

dans le fichier requirements.txt se trouve python-dotenv

ce qui vaut a faire un pip install python-dotenv

A la racine de votre git créer un fichier .env

et coller

FLASK_APP=app.py
FLASK_ENV=development
DEBUG = True

# Démarrer le projet
cd app

flask run

le projet est démarrer dans un environnement de développement avec le debug actif
