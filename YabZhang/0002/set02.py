#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mysql

db = mysql.connect(host="localhost", user="root")
cursor = db.cursor()

sqla = """CREATE DATABASE IF NOT EXISTS test;"""
sqlb = """CREATE TABLE IF NOT EXISTS mycode ( code char(20) not null);"""
sqlc = """INSERT INTO mycode (code) VALUES ("%s");"""

cursor.execute(sqla)
cursor.execute("""USE test;""")
cursor.execute(sqlb)
with open("keys.txt", 'r') as f:
    try:
        for code in f:
            code = code.strip()
            cursor.execute(sqlc % code)
        print "Done!"
    except:
        print "Error!"
    finally:
        cursor.close()
        db.commit()
        db.close()

