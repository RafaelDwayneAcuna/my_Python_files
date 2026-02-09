print("MY BIO DATA")


while True:
    name = input("Enter your name in uppercases: ")
    if name.isupper():
        print("Hello, " + name)
        break
    else:
        print("please enter your name in capital letters")

address = input("Are you from Makati? (Y/N): ").upper()

if address == "Y":
    print("You are a makatizen")
else:
    print("You are not from makati")

age = int(input("Enter age: "))

if age < 18:
    print("You are underage")
else:
    print("You are of legal age")

gender = input("MALE/FEMALE: ").upper()

if gender == "MALE":
    print("You are a male")
else:
    print("you are a female")

birthday = int(input("Enter your birth year: "))

# it is currently 2/3/2026

if birthday == 2000:
    print("You are/turning 26 this year")
elif birthday == 2001:
    print("You are/turning 25 this year")
elif birthday == 2002:
    print("You are/turning 24 this year")
elif birthday == 2003:
    print("You are/turning 23 this year")
elif birthday == 2004:
    print("You are/turning 22 this year")
elif birthday == 2005:
    print("You are/turning 21 this year")
elif birthday == 2006:
    print("You are/turning 20 this year")
elif birthday == 2007:
    print("You are/turning 19 this year")
elif birthday == 2008:
    print("You are/turning 18 this year")
else:
    print("You are currently underage")


course = input("Enter your course: ")
print(f"You are from {course}")

status = input("Enter your status (single/taken): ")

if status == "single":
    print("wala kang jowa")
else:
    print("meron kang ea")

religion = input("Enter your religion: ")
print(f"You are {religion}")

hobby = input("Enter your hobby/hobbies: ")
print(f"your hobbies are {hobby}")

skills = input("Enter your skills/talents: ")
print(skills)



# print(
#    " My name is " + name + ". I live in " + address + " I am a " + age + "," + gender + " My  Birthday is " + birthday + " And my course is " + course + "I am " + status + " I am a " + religion + " And My hobby is " + hobby + " And my Skills are " + skills
#   )

