import controller.request as request

def add_sujet(data):
    if (data["sujet"] == ""):
        return False

    requete = "INSERT INTO sujet (sujet) VALUES (?);"
    request.insert_in_db(requete, (data["sujet"],))

    return True

def get_all_sujet():
    json = request.select_from_db("SELECT * FROM sujet")
    
    return json

def get_sujet(id):
    if (not id):
        return False

    json = request.select_from_db("SELECT * FROM sujet WHERE sujet_id = ?", (id,))

    if len(json) > 0:
        return json[0]
    else:
        return []

def delete_sujet(id):
    if (not id):
        return False

    request.delete_from_db("DELETE FROM sujet WHERE sujet_id = ?", (id,))

    return True