#Ask the user input------------------------------
user_input = input("Is this a palindrome? Enter a word to find out!: ")

#this translates to pal = user's response
pal = user_input

#start index is 0=firstletter
#end index is whatever the length is of word 
start_index = 0
end_index = len(pal) - 1

#making sure that both operands are equal.
#anytime either of the operands are not equal,the loop will break
while start_index <= end_index:
    if pal[start_index] != pal[end_index]:
        break

    start_index += 1
    end_index -= 1
#response to the user
if start_index >= end_index:
    print(user_input,"is a palindrome!")

else:
    print(user_input,"is not a palindrome!")
    
