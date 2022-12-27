import controller.request as request

def add_categorie(data):
    if (data["titre"] == ""):
        return False
    
    if (not "ordre" in data):
        data["ordre"] = None

    if (not "visible" in data):
        data["visible"] = True

    requete = "INSERT INTO categorie (titre, ordre, visible) VALUES (?, ?, ?);"
    request.insert_in_db(requete, (data["titre"], data["ordre"], data["visible"]))

    return True

def get_all_categorie():
    json = request.select_from_db("SELECT * FROM categorie")
    
    return json

def get_categorie(id):
    if (not id):
        return False

    json = request.select_from_db("SELECT * FROM categorie WHERE categorie_id = ?", (id,))

    if len(json) > 0:
        return json[0]
    else:
        return []

def delete_categorie(id):
    if (not id):
        return False

    request.delete_from_db("DELETE FROM categorie WHERE categorie_id = ?", (id,))

    return True