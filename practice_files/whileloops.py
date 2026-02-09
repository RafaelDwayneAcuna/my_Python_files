
# WHILE NOT
# WHILE
# WHILE THIS OR THIS
# WHILE TRUE

import random

secret_number = random.randint(1, 99)

guess = int(input("Enter your guessed number 1-99: "))

while guess != secret_number:
    
    if guess < 1:
        print("You went over the limit")
        guess = int(input("Enter your guessed number 1-99: "))
    elif guess > 99:
        print("You went over the limit")
        guess = int(input("Enter your guessed number 1-99: "))
    else:
        print("Wrong")
        guess = int(input("Enter your guessed number 1-99: "))
        


print("Congratulations, You've guessed correct")







