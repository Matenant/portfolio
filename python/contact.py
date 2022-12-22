import mariadb
import json

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
    print(requete)
    cur, conn = get_db_connection()
    print(requete)
    cur.execute(requete, data)

    conn.commit()
    conn.close()

def select_from_db(requete, data=()):
    cur, conn = get_db_connection()

    cur.execute(requete, data)
    print(cur.description,flush=True)
    records = cur.fetchall()

    conn.close()
    return records

def add_sujet(data):
    if (data["subject"] == ""):
        return False

    requete = "INSERT INTO sujet (subject) VALUES (?);"
    insert_in_db(requete, (data["subject"],))

    return True

def get_all_sujet():

    json = select_from_db("SELECT * FROM sujet")
    print(json)
    return json

def get_sujet(id):
    cur, conn = get_db_connection()

    cur.execute("SELECT * FROM sujet")

    records = cur.fetchall()
    for row in records:
        print(row, flush=True)
    conn.close()
    return records