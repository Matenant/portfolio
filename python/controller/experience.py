import controller.request as request

def add_experience(data):
  if (not "titre" in data or data["titre"] == "" or not "categorie_id" in data or data["categorie_id"] == "" or not "description" in data or data["description"] == ""):
    return False
  
  if (not "ordre" in data):
    data["ordre"] = None

  if (not "visible" in data):
    data["visible"] = True

  requete = "INSERT INTO experience (titre, description, categorie_id, ordre, visible) VALUES (?, ?, ?, ?, ?);"
  new_id = request.insert_in_db(requete, (data["titre"], data["description"], data["categorie_id"], data["ordre"], data["visible"]))

  if ("technologies" in data):
    for technologie in data["technologies"]:
      request.insert_in_db("INSERT INTO experience_technologie (experience_id, technologie_id) VALUES (?, ?);", (new_id, technologie))

  if ("remarques" in data):
    for remarque in data["remarques"]:
      request.insert_in_db("INSERT INTO remarque (experience_id, remarque) VALUES (?, ?);", (new_id, remarque))

  return True

def get_all_experience():
  json = request.select_from_db("SELECT * FROM experience")

  for element in json:
    # Categorie
    element["categorie"] = request.select_from_db("SELECT * FROM categorie WHERE categorie_id = (?)", (element["categorie_id"],))[0]
    # Technologies
    element["technologies"] = request.select_from_db("SELECT technologie.technologie_id, technologie.created, technologie.modified, technologie.titre FROM experience_technologie, technologie WHERE experience_technologie.experience_id = (?) AND technologie.technologie_id = experience_technologie.technologie_id", (element["experience_id"],))
    #Remarques
    element["remarques"] = request.select_from_db("SELECT * FROM remarque WHERE remarque.experience_id = (?)", (element["experience_id"],))

  if len(json) > 0:
    return json
  else:
    return []

def get_experience(id):
  if (not id):
    return False

  json = request.select_from_db("SELECT * FROM experience WHERE experience_id = ?", (id,))

  if len(json) > 0:
    # Categorie
    json[0]["categorie"] = request.select_from_db("SELECT * FROM categorie WHERE categorie_id = (?)", (json[0]["categorie_id"],))[0]
    # Technologies
    json[0]["technologies"] = request.select_from_db("SELECT technologie.technologie_id, technologie.created, technologie.modified, technologie.titre FROM experience_technologie, technologie WHERE experience_technologie.experience_id = (?) AND technologie.technologie_id = experience_technologie.technologie_id", (json[0]["experience_id"],))

    return json[0]
  else:
    return []

def delete_experience(id):
  if (not id):
    return False

  request.delete_from_db("DELETE FROM experience_technologie WHERE experience_id = ?", (id,))
  request.delete_from_db("DELETE FROM remarque WHERE experience_id = ?", (id,))

  request.delete_from_db("DELETE FROM experience WHERE experience_id = ?", (id,))

  return True