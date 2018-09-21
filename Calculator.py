# Assignment 1---------------------------------------------
def calculator():
    first_number = int(input("Enter a number: "))
    operator = input("Enter an operator: ")
    ops = ["+","-","*","/"]
    if operator in ops:
        second_number = int(input("Enter another number: "))
    else:
        print("Sorry," + "'" + operator + "'"+ " is not valid.")
        quit_prompt = input("Press Q to quit OR enter to try again: ")
        q_button = ["Q","q"]
        if quit_prompt in q_button:
            quit()
        
        print(calculator())

    def sub(number1,number2):
        print(number1 + number2)

    if operator == "+":
        sub(first_number,second_number)
    
    def sub(number1,number2):
        print(number1 - number2)

    if operator == "-":
        sub(first_number,second_number)

    def multi(number1,number2):
        print(number1 * number2)

    if operator == "*":
         multi(first_number,second_number)

    def div(number1,number2):
        print(number1 / number2)

    if operator == "/":
        div(first_number,second_number)

calculator() 
