import sqlite3

connection = sqlite3.connect("itstep_DBB.sl4", 5)
cur = connection.cursor()

cur.execute("INSERT INTO second_table (name) VALUES ('Androsenko');")
cur.execute("INSERT INTO second_table (name) VALUES ('Stanislav');")
connection.commit()

connection.close()