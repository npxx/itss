import sqlite3
conn = sqlite3.connect('students.db')
print("Opened database successfully");
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT)')
print("Table created successfully");
conn.close()