

def start_program():

    print("HELLO AND WELCOME TO THE PROGRAM!")
    print(" ")

    print("1. Check even/odd \n2. Add two numbers \n3. exit")

    choice = input("\nEnter your choice: ")

    def even_odd_checker(number):
        if number % 2 == 0:
            print("This number is even.")
        else:
            print("This number is odd.")

    if choice == "1":
       
        choice2 = input(print("Would you like to try the even or odd check? (Y/N): ")).upper()
        if choice2 == "Y":
            number = int(input("Please enter number: "))
            even_odd_checker(number)

        elif choice2 == "N": 
            start_program()

    elif choice == "2":
        numInput = int(input("Please enter the 1st number: "))
        numInput2 = int(input("Please enter the 2nd number: "))
        
        total = numInput + numInput2
        print(f"Your added numbers are: \n{total}")

    elif choice == "3":
        exit()

start_program()