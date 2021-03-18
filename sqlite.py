import sqlite3

connect = sqlite3.connect("test.db")
cursor = connect.cursor()
# cursor.execute("CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))")
# cursor.execute('INSERT INTO user (id, name) VALUES (\'2\', \'Michael\')')
cursor.execute("select * from user")
print(cursor.fetchall())
cursor.close()

connect.commit()
connect.close()
