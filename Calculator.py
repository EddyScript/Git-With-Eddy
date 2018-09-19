first_number =  int(input("Put a number here: "))
operator = input("Put a math operator: ")
second_number = int(input("Put a second number: "))

def add(number1,number2):
    print(number1 + number2)

def sub(number1,number2):
    print(number1 - number2)

def multi(number1,number2):
    print(number1 * number2)
    
def div(number1,number2):
    print(number1 / number2)


if operator == "+":
    add(first_number,second_number)

if operator == "-":
    sub(first_number,second_number)

if operator == "*":
    multi(first_number,second_number)

if operator == "/":
    div(first_number,second_number)
