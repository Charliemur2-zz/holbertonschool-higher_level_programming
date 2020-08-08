#!/usr/bin/python3
import MySQLdb
import sys
arg = sys.argv

if __name__ == "__main__":
        db = MySQLdb.connect(host="localhost", user=arg[1], passwd=arg[2], db=arg[3], port=3306)
        cur = db.cursor()
        names = cur.execute("SELECT * FROM states ORDER BY states.id")
        names = cur.fetchall
        for item in names:
            print(item)
        db.close()