import mariadb
import sys
import re

try:
    conn = mariadb.connect(
        user="mysqlusr",
        password="mysqlpwd",
        host="database",
        port=3306,
        database="portfolio"
    )
    cur = conn.cursor()
    #code ici
    with open('create.sql') as f:
        fichier = f.read()
        lines = fichier.split(";")
        for index, line in enumerate(lines):
            if (line != ""):
                line = line.replace("\n", "")
                line = re.sub("\s+", " ", line)
                cur.execute(line)

except mariadb.Error as e:
    print(f"Erreur lors de la connection à la base de données: {e}")
    sys.exit(1)