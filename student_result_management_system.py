import mysql.connector

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sathwik@4036", 
    database="student_db"
)

cursor = db.cursor()

def add_student():
    print("\n--- ADD STUDENT ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    math = float(input("Enter Math Marks: "))
    science = float(input("Enter Science Marks: "))
    english = float(input("Enter English Marks: "))
    
    # Calculate Total, Average, and Pass Fail Status
    total = math + science + english
    avg = total / 3
    
    if math >= 40 and science >= 40 and english >= 40:
        status = "PASS"
    else:
        status = "FAIL"
        
    query = "INSERT INTO students (roll_number, name, math_marks, science_marks, english_marks, total_marks, average_marks, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (roll, name, math, science, english, total, avg, status)
    
    cursor.execute(query, values)
    db.commit()
    print("Student added successfully!")

def calculate_class_average():
    print("\n--- CLASS AVERAGE ---")
    query = "SELECT AVG(average_marks) FROM students"
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result[0] is not None:
        print("Overall Class Average:", round(result[0], 2))
    else:
        print("No student records found.")

def find_topper():
    print("\n--- CLASS TOPPER ---")
    query = "SELECT roll_number, name, total_marks FROM students ORDER BY total_marks DESC LIMIT 1"
    cursor.execute(query)
    topper = cursor.fetchone()
    
    if topper:
        print("Roll No:", topper[0])
        print("Name:", topper[1])
        print("Total Marks:", topper[2])
    else:
        print("No student records found.")

def generate_report():
    print("\n--- PASS / FAIL REPORT ---")
    query = "SELECT roll_number, name, total_marks, average_marks, status FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    
    if not students:
        print("No student records found.")
        return

    print("Roll No | Name | Total | Average | Status")
    print("-" * 45)
    
    pass_count = 0
    fail_count = 0
    
    for s in students:
        print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]:.2f} | {s[4]}")
        if s[4] == "PASS":
            pass_count += 1
        else:
            fail_count += 1
            
    print("-" * 45)
    print("Passed:", pass_count, "| Failed:", fail_count)

# Main Loop
while True:
    print("\n=== STUDENT RESULT SYSTEM ===")
    print("1. Add Student Marks")
    print("2. Show Class Average")
    print("3. Show Class Topper")
    print("4. Show Pass/Fail Report")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        calculate_class_average()
    elif choice == "3":
        find_topper()
    elif choice == "4":
        generate_report()
    elif choice == "5":
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice, try again.")

# Close connection on exit
cursor.close()
db.close()