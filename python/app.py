from flask import Flask, jsonify, request
import mariadb
import contact

app = Flask(__name__)

@app.get('/')
def hello_world():
    return 'Hello, Docker !'


@app.post('/addSubject')
def addSubject():
    json = request.get_json()
    if (contact.add_sujet(json)):
        return "Element ajouté.", 200
    return "Erreur", 400

@app.get('/getAllSubject')
def getAllSubject():
    result = contact.get_all_sujet()
    return result