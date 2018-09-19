num = int(input("Enter a number for a factorial: "))

factorial = 1

if num < 0:
    print("Please insert a positive number")

else:
    for result in range(1,num + 1):
        factorial = factorial*result
    print("the factorial for",num, "=" ,factorial)

    
