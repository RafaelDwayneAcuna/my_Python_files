
usernames = {"rafa", "admin", "guest"}

def start_program():
 print("\nUnique Username Checker\n")

 print(f"Current usernames are {usernames}")

 choice = input("Enter a user name: ")

 if choice == "rafa":
     print("Sorry the username is taken")
     choice2 = input("Would you like to try again? (Y/N): ").upper()
     if choice2 == "Y":
        start_program()
     elif choice2 == "N":
        exit()
     else:
        print("Choose only Y or N")
 elif choice == "admin":
     print("Sorry this username is taken")
     choice2 = input("Would you like to try again? (Y/N): ").upper()
     if choice2 == "Y":
        start_program()
     elif choice2 == "N":
        exit()
     else:
        print("Choose only Y or N")
 elif choice == "guest":
     print("Sorry the username is also taken")
     choice2 = input("Would you like to try again? (Y/N): ").upper()
     if choice2 == "Y":
        start_program()
     elif choice2 == "N":
        exit()
     else:
        print("Choose only Y or N")
 else:
     usernames.add(choice)
     print("Username added")
     print(usernames)

start_program()


