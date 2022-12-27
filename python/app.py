from flask import Flask, jsonify, request
import controller.sujet as sujet
import controller.contact as contact

import controller.categorie as categorie

app = Flask(__name__)

@app.get('/')
def hello_world():
    return 'Hello, Docker !'

#Subject
@app.post('/sujet')
def addSubject():
    json = request.get_json()
    if (sujet.add_sujet(json)):
        return "Element ajouté.", 200
    return "Erreur", 400

@app.get('/sujet')
def getAllSubject():
    result = sujet.get_all_sujet()
    return result

@app.get('/sujet/<int:index>')
def getSubject(index):
    result = sujet.get_sujet(index)
    return result

@app.delete('/sujet/<int:index>')
def deleteSubject(index):
    if (sujet.delete_sujet(index)):
        return "Element supprimé.", 200
    return "Erreur", 400

#Contact
@app.post('/contact')
def addContact():
    json = request.get_json()
    if (contact.add_contact(json)):
        return "Element ajouté.", 200
    return "Erreur", 400

@app.get('/contact')
def getAllContact():
    result = contact.get_all_contact()
    return result

@app.get('/contact/<int:index>')
def getContact(index):
    result = contact.get_contact(index)
    return result

@app.delete('/contact/<int:index>')
def deleteContact(index):
    if (contact.delete_contact(index)):
        return "Element supprimé.", 200
    return "Erreur", 400

#Categorie
@app.post('/categorie')
def addCategorie():
    json = request.get_json()
    if (categorie.add_categorie(json)):
        return "Element ajouté.", 200
    return "Erreur", 400

@app.get('/categorie')
def getAllCategorie():
    result = categorie.get_all_categorie()
    return result

@app.get('/categorie/<int:index>')
def getCategorie(index):
    result = categorie.get_categorie(index)
    return result

@app.delete('/categorie/<int:index>')
def deleteCategorie(index):
    if (categorie.delete_categorie(index)):
        return "Element supprimé.", 200
    return "Erreur", 400