import controller.request as request

def add_technologie(data):
    if (not "titre" in data or data["titre"] == ""):
        return False

    requete = "INSERT INTO technologie (titre) VALUES (?);"
    request.insert_in_db(requete, (data["titre"],))

    return True

def get_all_technologie():
    json = request.select_from_db("SELECT * FROM technologie")
    
    return json

def get_technologie(id):
    if (not id):
        return False

    json = request.select_from_db("SELECT * FROM technologie WHERE technologie_id = ?", (id,))

    if len(json) > 0:
        return json[0]
    else:
        return []

def delete_technologie(id):
    if (not id):
        return False

    request.delete_from_db("DELETE FROM technologie WHERE technologie_id = ?", (id,))

    return True