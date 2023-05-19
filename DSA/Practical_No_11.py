import os
def add_student():
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    division = input("Enter division: ")
    address = input("Enter address: ")
    with open("student_info.txt", "a") as file:
        file.write(f"{roll_number},{name},{division},{address}\n")
    print("Student information added successfully.")

def delete_student():
    roll_number = input("Enter roll number to delete: ")
    with open("student_info.txt", "r") as file:
        lines = file.readlines()
    with open("student_info.txt", "w") as file:
        deleted = False
        for line in lines:
            if line.startswith(roll_number + ','):
                deleted = True
                continue
            file.write(line)
    if deleted:
        print("Student information deleted successfully.")
    else:
        print("Student not found.")

def display_student():
    roll_number = input("Enter roll number to display: ")
    with open("student_info.txt", "r") as file:
        found = False
        for line in file:
            if line.startswith(roll_number + ','):
                found = True
                roll_number, name, division, address = line.strip().split(',')
                print("Roll Number:", roll_number)
                print("Name:", name)
                print("Division:", division)
                print("Address:", address)
                break
    if not found:
        print("Student not found.")
while True:
    print("Menu:")
    print("1. Add Student Information")
    print("2. Delete Student Information")
    print("3. Display Student Information")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        delete_student()
    elif choice == '3':
        display_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
