
number = int(input("enter a number: "))

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
    
result = check_even_odd(number)
print(result)

num = int(input("Enter a number: "))

def check_positive_or_negative(num):
    if num > 0:
        return "Positive"
    else:
        return "Negative or Zero"

result = check_positive_or_negative(num)
print(result)
