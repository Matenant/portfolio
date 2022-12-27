import mariadb

def get_db_connection():
    conn = mariadb.connect(
        user="mysqlusr",
        password="mysqlpwd",
        host="database",
        port=3306,
        database="portfolio"
    )
    cur = conn.cursor()
    return cur, conn

def insert_in_db(requete, data=()):
    cur, conn = get_db_connection()
    
    cur.execute(requete, data)

    conn.commit()
    conn.close()

def select_from_db(requete, data=()):
    cur, conn = get_db_connection()
    
    cur.execute(requete, data)
    records = cur.fetchall()

    field_names = [i[0] for i in cur.description]
    result = []
    for record in records:
        element = {}
        for key, value in enumerate(record):
            element[field_names[key]] = value
        result.append(element)

    conn.close()
    return result

def delete_from_db(requete, data=()):
    cur, conn = get_db_connection()
    
    cur.execute(requete, data)

    conn.commit()
    conn.close()