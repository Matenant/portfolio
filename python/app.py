from flask import Flask, jsonify, request
import controller.sujet as sujet
import controller.contact as contact

import controller.categorie as categorie
import controller.experience as experience
import controller.technologie as technologie
import controller.remarque as remarque

app = Flask(__name__)

@app.get('/')
def hello_world():
    return 'Hello, Docker !'

# Subject
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

# Contact
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

# Categorie
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

# Experience
@app.post('/experience')
def addExperience():
    json = request.get_json()
    if (experience.add_experience(json)):
        return "Element ajouté.", 200
    return "Erreur", 400

@app.get('/experience')
def getAllExperience():
    result = experience.get_all_experience()
    return result

@app.get('/experience/<int:index>')
def getExperience(index):
    result = experience.get_experience(index)
    return result

@app.delete('/experience/<int:index>')
def deleteExperience(index):
    if (experience.delete_experience(index)):
        return "Element supprimé.", 200
    return "Erreur", 400

# Technologie
@app.post('/technologie')
def addTechnologie():
    json = request.get_json()
    if (technologie.add_technologie(json)):
        return "Element ajouté.", 200
    return "Erreur", 400

@app.get('/technologie')
def getAllTechnologie():
    result = technologie.get_all_technologie()
    return result

@app.get('/technologie/<int:index>')
def getTechnologie(index):
    result = technologie.get_technologie(index)
    return result

@app.delete('/technologie/<int:index>')
def deleteTechnologie(index):
    if (technologie.delete_technologie(index)):
        return "Element supprimé.", 200
    return "Erreur", 400

# Remarque
@app.delete('/remarque/<int:index>')
def deleteRemarque(index):
    if (remarque.delete_remarque(index)):
        return "Element supprimé.", 200
    return "Erreur", 400