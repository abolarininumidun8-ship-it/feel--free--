# 1
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = input("Enter age: ")
gender = input("Enter gender: ")

with open("students.txt", "w") as file:
    file.write(f"First Name: {first_name}\n")
    file.write(f"Last Name: {last_name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Gender: {gender}\n")
    file.write("-------------\n")
print("Student details saved to students.txt\n")


# 2
name = input("Enter student name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")
address = input("Enter home address: ")

with open("contact.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Phone: {phone}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Address: {address}\n")
    file.write("-------------\n")
print("Contact details saved to contact.txt\n")


# 3
name = input("Enter student name: ")
school = input("Enter school name: ")
student_class = input("Enter class: ")
subject = input("Enter favourite subject: ")

with open("school.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"School: {school}\n")
    file.write(f"Class: {student_class}\n")
    file.write(f"Favourite Subject: {subject}\n")
    file.write("-------------\n")
print("School information saved to school.txt\n")


# 4
print("--- Reading students.txt ---")
with open("students.txt", "r") as file:
    content = file.read()
    print(content)


# 5
first_name = input("Enter another student's first name: ")
last_name = input("Enter last name: ")
age = input("Enter age: ")
gender = input("Enter gender: ")

with open("students.txt", "a") as file:
    file.write(f"First Name: {first_name}\n")
    file.write(f"Last Name: {last_name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Gender: {gender}\n")
    file.write("-------------\n")
print("New student appended to students.txt\n")


# 6
name = input("Enter student name: ")
math_score = input("Enter Mathematics score: ")
english_score = input("Enter English score: ")
computer_score = input("Enter Computer Studies score: ")

with open("results.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Mathematics: {math_score}\n")
    file.write(f"English: {english_score}\n")
    file.write(f"Computer Studies: {computer_score}\n")
    file.write("-------------\n")
print("Results saved to results.txt\n")


# 7
for i in range(1, 6):
    print(f"Enter details for Student {i}:")
    name = input("Name: ")
    age = input("Age: ")
    student_class = input("Class: ")
    
    with open("class_records.txt", "a") as file:
        file.write(f"Student {i} - Name: {name}, Age: {age}, Class: {student_class}\n")
print("All 5 students saved to class_records.txt\n")



# 8
name = input("Enter student name: ")
reg_no = input("Enter registration number: ")
department = input("Enter department: ")
level = input("Enter level: ")

with open("registration.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Reg Number: {reg_no}\n")
    file.write(f"Department: {department}\n")
    file.write(f"Level: {level}\n")
    file.write("-------------\n")
print("Registration saved to registration.txt\n")



# 9
name = input("Enter student name: ")
age = input("Enter age: ")
hobbies = input("Enter hobbies: ")
ambition = input("Enter career ambition: ")

with open("bio.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Hobbies: {hobbies}\n")
    file.write(f"Career Ambition: {ambition}\n")
    file.write("-------------\n")

print("\n--- Displaying bio.txt ---")
with open("bio.txt", "r") as file:
    print(file.read())



# 10
while True:
    print("\n=== Student Record Management System ===")
    print("1. Register a student")
    print("2. View all registered students")
    print("3. Exit")
    
    choice = input("Choose an option (1, 2, or 3): ")
    
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter student course: ")
        
        with open("students.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Course: {course}\n")
            file.write("-------------\n")
        print("Student registered successfully!")
        
    elif choice == "2":
        print("\n--- All Registered Students ---")
        with open("students.txt", "r") as file:
            print(file.read())
            
    elif choice == "3":
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice. Please try again.")