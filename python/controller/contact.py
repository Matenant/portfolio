import controller.request as request


def add_contact(data):
    if (data["sujet_id"] == "" or data["description"] == "" or data["mail"] == ""):
        return False

    if (not "soussujet" in data):
        data["soussujet"] = ""

    requete = "INSERT INTO contact (sujet_id, description, mail, soussujet) VALUES (?, ?, ?, ?);"
    request.insert_in_db(requete, (data["sujet_id"], data["description"], data["mail"], data["soussujet"]))

    return True

def get_all_contact():
    json = request.select_from_db("SELECT * FROM contact")
    
    return json

def get_contact(id):
    if (not id):
        return False

    json = request.select_from_db("SELECT * FROM contact WHERE contact_id = ?", (id,))

    if len(json) > 0:
        return json[0]
    else:
        return []

def delete_contact(id):
    if (not id):
        return False

    request.delete_from_db("DELETE FROM contact WHERE contact_id = ?", (id,))

    return True