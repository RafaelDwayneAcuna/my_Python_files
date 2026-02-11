
student_scores = [80, 40, 60, 33, 34, 70]

while True:
    
    print("\nSTUDENT SCORES MANAGER\n")

    print(f"Current Scores: {student_scores}")

    print("\nEnter 1 to add a new score")
    print("Enter 2 to remove a score")
    print(("Enter 3 to print updated score"))

    choice = input("Enter your choice: ")


    if choice == "1":
        newscore = int(input("Enter a new score: "))
        student_scores.append(newscore)
        print(student_scores)

    elif choice == "2":
        removescore = int(input("Enter number you wanna delete: "))
        student_scores.remove(removescore)










