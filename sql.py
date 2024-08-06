import sqlite3

# Connect to sqlite3
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table, retrieve result
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

# Insert some records
cursor.execute("INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('Sudhanshu', 'Data Science', 'B', 100)")
cursor.execute("INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'A', 86)")
cursor.execute("INSERT INTO STUDENT VALUES ('Vikash', 'DEVOPS', 'A', 50)")
cursor.execute("INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'A', 35)")
cursor.execute("INSERT INTO STUDENT VALUES ('Aisha', 'Data Science', 'A', 95)")
cursor.execute("INSERT INTO STUDENT VALUES ('John', 'Data Science', 'B', 89)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ravi', 'Data Science', 'C', 78)")
cursor.execute("INSERT INTO STUDENT VALUES ('Nina', 'DEVOPS', 'B', 60)")
cursor.execute("INSERT INTO STUDENT VALUES ('Suresh', 'DEVOPS', 'C', 45)")
cursor.execute("INSERT INTO STUDENT VALUES ('Maya', 'AI', 'A', 92)")
cursor.execute("INSERT INTO STUDENT VALUES ('Alex', 'AI', 'B', 85)")
cursor.execute("INSERT INTO STUDENT VALUES ('Emily', 'AI', 'C', 76)")
cursor.execute("INSERT INTO STUDENT VALUES ('Raj', 'Cyber Security', 'A', 88)")
cursor.execute("INSERT INTO STUDENT VALUES ('Sophia', 'Cyber Security', 'B', 82)")
cursor.execute("INSERT INTO STUDENT VALUES ('Liam', 'Cyber Security', 'C', 70)")
cursor.execute("INSERT INTO STUDENT VALUES ('Zara', 'Cloud Computing', 'A', 94)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ethan', 'Cloud Computing', 'B', 80)")
cursor.execute("INSERT INTO STUDENT VALUES ('Olivia', 'Cloud Computing', 'C', 65)")
cursor.execute("INSERT INTO STUDENT VALUES ('Lucas', 'Machine Learning', 'A', 91)")
cursor.execute("INSERT INTO STUDENT VALUES ('Grace', 'Machine Learning', 'B', 87)")
cursor.execute("INSERT INTO STUDENT VALUES ('Mason', 'Machine Learning', 'C', 73)")
cursor.execute("INSERT INTO STUDENT VALUES ('Hannah', 'Data Science', 'A', 92)")
cursor.execute("INSERT INTO STUDENT VALUES ('Karan', 'Data Science', 'B', 84)")
cursor.execute("INSERT INTO STUDENT VALUES ('Priya', 'Data Science', 'C', 77)")
cursor.execute("INSERT INTO STUDENT VALUES ('Arjun', 'DEVOPS', 'A', 55)")
cursor.execute("INSERT INTO STUDENT VALUES ('Neha', 'DEVOPS', 'B', 62)")
cursor.execute("INSERT INTO STUDENT VALUES ('Sam', 'AI', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('Tina', 'AI', 'B', 83)")
cursor.execute("INSERT INTO STUDENT VALUES ('Omar', 'AI', 'C', 74)")
cursor.execute("INSERT INTO STUDENT VALUES ('Anya', 'Cyber Security', 'A', 89)")
cursor.execute("INSERT INTO STUDENT VALUES ('Leo', 'Cyber Security', 'B', 81)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ava', 'Cyber Security', 'C', 72)")
cursor.execute("INSERT INTO STUDENT VALUES ('Jack', 'Cloud Computing', 'A', 93)")
cursor.execute("INSERT INTO STUDENT VALUES ('Emma', 'Cloud Computing', 'B', 79)")
cursor.execute("INSERT INTO STUDENT VALUES ('Noah', 'Cloud Computing', 'C', 66)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ryan', 'Machine Learning', 'A', 92)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ella', 'Machine Learning', 'B', 86)")
cursor.execute("INSERT INTO STUDENT VALUES ('David', 'Machine Learning', 'C', 75)")
cursor.execute("INSERT INTO STUDENT VALUES ('Sara', 'Big Data', 'A', 94)")
cursor.execute("INSERT INTO STUDENT VALUES ('Nathan', 'Big Data', 'B', 81)")
cursor.execute("INSERT INTO STUDENT VALUES ('Ivy', 'Big Data', 'C', 68)")
cursor.execute("INSERT INTO STUDENT VALUES ('Brian', 'Software Engineering', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('Carol', 'Software Engineering', 'B', 85)")
cursor.execute("INSERT INTO STUDENT VALUES ('Eve', 'Software Engineering', 'C', 73)")
cursor.execute("INSERT INTO STUDENT VALUES ('Tom', 'Blockchain', 'A', 88)")
cursor.execute("INSERT INTO STUDENT VALUES ('Nora', 'Blockchain', 'B', 83)")
cursor.execute("INSERT INTO STUDENT VALUES ('Oscar', 'Blockchain', 'C', 69)")

print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Commit your changes to the database
connection.commit()
connection.close()
