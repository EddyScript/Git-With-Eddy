#Assingment 1------------------------------------------------
family = ["Rambo","Jax","Oliver","Rambo","Lazy","Jarvis"]
family.remove("Rambo") #I could also use 'del family[0]' if it were a bigger list
print(family)
#Assingment 2 and 3------------------------------------------------
guitar_strings = [1,2,3,4,5,6]
bgs = len(guitar_strings)

def largest(guitar_strings,bgs):
    
    return max(guitar_strings)

print(largest(guitar_strings,bgs))

def smallest(guitar_strings,bgs):
    
    return min(guitar_strings)

print(smallest(guitar_strings,bgs))

#Assingment 4------------------------------------------------
num = int(input("Enter number of rows: "))
for a in range(0,num):# <--- number of rows
    for b in range(0,num-a-1):#<--- how many spaces in column
        print(end=" ")
    for b in range(0, a+1):#<--- how many stars in column
        print("*",end=" ")
    print()

