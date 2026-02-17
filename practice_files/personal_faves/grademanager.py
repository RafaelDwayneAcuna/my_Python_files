

student_data = {}

def start_program():

 print("\nSTUDENT GRADE MANAGER\n")

 print(f"\nCurrent data: {student_data}\n")

 print("Enter 1 to Add student")
 print("Enter 2 to View all students with corresponding grade")
 print("Enter 3 to Search student")
 print("Enter 4 to Exit")

 choice = input("\nEnter choice: ")

 if choice == "1":

     student = input("Enter student: ").capitalize()
     grade = input("Enter Student grade: ")
     student_data[student] = grade
     print(student_data)
     answer = input("Would you like to go back to main menu? (Y/N): ").upper().strip()
     if answer == "Y":
        start_program()
     else:
        exit()

 elif choice == "2":
    for student, grade in student_data.items():
       print(f"{student}: {grade}")
    answer = input("Would you like to go back to main menu? (Y/N): ").upper().strip()
    if answer == "Y":
        start_program()
    else:
        exit()

 elif choice == "3":
    searchedstudent = input("Enter student to be searched: ").capitalize()
    if searchedstudent in student_data:
       print(f"{searchedstudent}: {student_data[searchedstudent]}")
    else:
       print("Student not found")
    answer = input("Would you like to go back to main menu? (Y/N): ").upper().strip()
    if answer == "Y":
        start_program()
    else:
        exit()

 elif choice == "4":
    exit()

start_program()