
# python practice no. 3 

def start_ze_program():

 print("STUDENT GRADE CHECKER")

 student_score = int(input("\nEnter your score 0-100: "))

 def grade_checker():
     if student_score > 100:
         print("damn how??")
     elif student_score < 0:
         print("skill issue")
     elif student_score > 89:
         print("your Grade is A, Congrats")
     elif student_score > 79:
         print("your Grade is B, Well done")
     elif student_score > 69:
         print("your Grade is C, Not bad")
     elif student_score < 69:
         print("your Grade is an F, :( try harder")

 grade_checker()

 choice = input("\nWould you like to try again? (Y/N): ").upper()

 if choice == "Y":
     start_ze_program()
 elif choice == "N":
     exit()
 else:
     print("choose only Y/N")

start_ze_program()
    
 



