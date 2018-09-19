Pick_a_num = input("Even or Odd? Pick a number!: ")
their_response = int(Pick_a_num)

def even_or_odd(x):
    if(x % 10 ==0):
        print("Even")
    else:
        print("The Answer is...Odd")


even_or_odd(their_response)

