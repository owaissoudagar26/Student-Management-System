import mysql.connector

# connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # change if you use another username
    password="manu",
    database="student"
)

cursor = conn.cursor()

# Insert student
def add_student(rollno, name, department, marks):
    sql = """INSERT INTO students 
             (rollno, name, department, English, Maths, Science, SST, Hindi) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (rollno, name, department, marks[0], marks[1], marks[2], marks[3], marks[4])
    cursor.execute(sql, values)
    conn.commit()
    print("Student added successfully!")

# Display all students
def display_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(f"Roll No: {row[0]}, Name: {row[1]}, Dept: {row[2]}, "
              f"English: {row[3]}, Maths: {row[4]}, Science: {row[5]}, SST: {row[6]}, Hindi: {row[7]}")
while True:
    print("\n--- Student Database Menu ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rollno = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        marks = []
        for subject in ["English", "Maths", "Science", "SST", "Hindi"]:
            marks.append(int(input(f"Enter marks in {subject}: ")))
        add_student(rollno, name, dept, marks)

    elif choice == "2":
        display_students()

    elif choice == "3":
        conn.close()
        print("Connection closed. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

