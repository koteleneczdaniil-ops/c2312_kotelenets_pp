import sqlite3

connection = sqlite3.connect("itstep_DBB.sl4", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE second_table (name TEXT);")
connection.commit()

connection.close()