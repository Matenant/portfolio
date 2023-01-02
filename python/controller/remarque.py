import controller.request as request

def delete_remarque(id):
  if (not id):
    return False

  request.delete_from_db("DELETE FROM remarque WHERE remarque_id = ?", (id,))

  return True