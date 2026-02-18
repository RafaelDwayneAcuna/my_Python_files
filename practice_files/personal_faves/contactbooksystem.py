
contacts = {
    "Rafael": "09123456789"
}

def start_program():
 
 def add_contact():
     name = input("Enter the contact name: ").capitalize()
     number = input("Enter contact number: ")
     contacts[name] = number
     print("\nContact has been added\n")
     print(f"Currect contacts: {contacts}")

 def validation():
     answer = input("Would you like to go back to main menu? (Y/N): ").upper()
     if answer == "Y":
        start_program()
     else:
        exit()

 print("\nContact Book System\n")

 print(f"\nCurrent contacts {contacts}\n")

 print("Enter 1 to Add contact")
 print("Enter 2 to View all contacts")
 print("Enter 3 to Search contact")
 print("Enter 4 to Delete contact")
 print("Enter 5 to Exit")

 choice = input("\nEnter your choice: ")

 if choice == "1":
     add_contact()
     validation()

 elif choice == "2":
    print("\nAll contacts\n")
    for name, number in contacts.items():
       print(f"{name}: {number}")

    validation()
 
 elif choice == "3":
    searchcontact = input("Enter contact name to search: ").capitalize().strip()
    if searchcontact in contacts:
       print("\nContact found!\n")
       print(f"{searchcontact}: {contacts[searchcontact]}")
    else:
       print("Contact not found")
    
    validation()

 elif choice == "4":
    deletecontact = input("Enter contact name to delete: ").capitalize().strip()
    if deletecontact in contacts:
       del contacts[deletecontact]
       print("\nContact has been deleted!\n")
       print(f"\nCurrent contacts: {contacts}\n")
    else:
       print("Contact not found")
    
    validation()



start_program()