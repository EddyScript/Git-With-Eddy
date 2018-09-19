def FizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0: 
        print("Buzz")

num = int(input("Pick a number!"))

FizzBuzz(num)
