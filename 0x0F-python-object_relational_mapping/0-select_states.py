#!/usr/bin/python3
import MySQLdb
import sys
arg = sys.argv

if __name__ == "__main__":
        db = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
        cur = db.cursor()
        name = cur.execute("SELECT * FROM %s" % arg[3])
        print("%d, %s" % states.id, name)
        db.close()
