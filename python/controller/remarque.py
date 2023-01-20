import controller.request as request

def add_remarque(data):

  if (not "experience_id" in data or not "remarque" in data):
    return False
  
  request.insert_in_db("INSERT INTO remarque (experience_id, remarque) VALUES (?, ?);", (data["experience_id"], data["remarque"]))
  
  return True

def update_remarque(data):

  if (not "remarque_id" in data or not "remarque" in data):
    return False
  
  request.update_from_db("UPDATE remarque SET remarque = ? WHERE remarque_id = ?;", (data["remarque"], data["remarque_id"]))
  
  return True

def delete_remarque(id):
  if (not id):
    return False

  request.delete_from_db("DELETE FROM remarque WHERE remarque_id = ?", (id,))

  return True