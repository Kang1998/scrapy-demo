# -*- coding: utf-8 -*-

import pymysql

db = pymysql.connect("localhost", "root", "cwk646202", "spider")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()