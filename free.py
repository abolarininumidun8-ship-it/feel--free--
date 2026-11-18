
# # 1
# print("File handling refers to the process of creating, opening, reading, writing, and closing files stored on a computer's storage system using Python. It allows programs to store and retrieve data permanently, meaning the information is saved even after the program stops running.")

# # 2
# print("Writing (\"w\"): Opens a file for writing. If the file already exists, it completely overwrites (erases) all previous content and starts fresh. If the file does not exist, it creates a new file.")
# print("Appending (\"a\"): Opens a file for writing, but adds new content to the end of the file without deleting or altering any of the existing content. If the file does not exist, it creates a new file.")

# # 3
# print("\"r\" (Read): Opens an existing file for reading content.")
# print("\"w\" (Write): Opens a file for writing. It clears existing data or creates a new file if none exists.")
# print("\"a\" (Append): Opens a file to add new data at the end without erasing existing content.")
# print("\"r+\" (Read and Write): Opens a file for both reading and writing operations starting from the beginning of the file.")

# # 4
# print("The open() function is used to open a file and return a file object. This object acts as a bridge between your Python program and the file on your computer, enabling you to perform actions like reading or writing.")

# # 5
# print("write(): This method writes a string of text or data into an open file.")
# print("close(): This method closes the open file. Closing a file frees up system resources (like memory) and ensures that all data is safely and properly written/saved to the hard drive.")

# # 6
# print("When you open an existing file in write mode ("w"), Python immediately clears or erases all existing content in that file, treating it as an empty file ready for new text.")

# 7

with open("student.txt", "w") as file:
    file.write("Name: Bella Smith\n")
    file.write("Age: 16\n")
    file.write("Course: Computer Science\n")

print("Student information saved successfully!")

name = input("Enter student name: ")
age = input("Enter Age: ")
course = input("Enter Course: ")


with open("contact.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Course: {course}\n")
    file.write("-------------\n")
print("Contact details saved to contact.txt\n")

# 8
with open("school.txt", "w") as file:
    file.write("Welcome to Python Programming Class.")

print("Sentence saved to school.txt successfully!")


# 9
with open("student.txt", "a") as file:
    file.write("Department: Science Department\n")
    file.write("Level: Grade 11\n")

print("Department and level appended successfully!")

# 10
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your home address: ")

# Save to details.txt
with open("details.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Home Address: {address}\n")

print("Details saved successfully in details.txt!")

# 11
with open("my_biography.txt", "w") as file:
    file.write("My name is Bella and I am 20 years old.\n")
    file.write("I have a strong passion for technology and coding.\n")
    file.write("In my free time, I love watching movies and reading novels.\n")
    file.write("My favorite subject in school is mathematics.\n")
    file.write("I hope to build my own tech startup in the future.\n")

print("Biography saved successfully!")


# 12

# Collect user input
fav_subject = input("Enter your favourite subject: ")
fav_food = input("Enter your favourite food: ")

# Open personal.txt in append mode ('a')
with open("personal.txt", "a") as file:
    file.write(f"Favourite Subject: {fav_subject}\n")
    file.write(f"Favourite Food: {fav_food}\n")

print("Your favorites have been appended to personal.txt!")