import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=2  ;")
connection.commit()

connection.close()