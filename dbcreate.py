import sqlite3
import random
import names
from faker import Faker

fake = Faker()

def create_database(num_records):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''CREATE TABLE IF NOT EXISTS records
                      (rollno NUMBER,
                       firstname TEXT,
                       lastname TEXT,
                       gender TEXT,
                       email TEXT,
                       city TEXT)''')

    # Generate and insert records
    for _ in range(num_records):
        firstname = names.get_first_name()
        lastname = names.get_last_name()
        gender = random.choice(['Male', 'Female'])
        email = fake.email()
        city = fake.city()

        rollno = random.randint(229000, 229999)
        while True:
            cursor.execute("SELECT * FROM records WHERE rollno=?", (rollno,))
            if cursor.fetchone() is None:
                break
            rollno = random.randint(229000, 229999)

        # Insert the record into the table
        cursor.execute("INSERT INTO records (rollno ,firstname, lastname, gender, email, city) VALUES (?, ?, ?, ?, ?, ?)",
                       (rollno, firstname, lastname, gender, email, city))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Example usage
num_records = 200
create_database(num_records)
