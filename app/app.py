from flask import Flask, render_template
from os import environ

#appel d'une clé test pour vérifié que celle-ci est bien reconnue.
#la clé se trouve dans le fichier .env
TEST_KEY = environ.get('TEST_KEY')
print(TEST_KEY) 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
