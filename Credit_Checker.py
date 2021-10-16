cardNo = list(input("What is your card number:))

check_number = cardNo.pop()    #this takes the number from the back and will make it our check number to use later
cardNo.reverse()       #reverses the code as it makes it easier for us to use the algorithm

changed_numbers = [] 

for index, number in enumerate(cardNo):     # This will check the wether or not the index is odd or even
    if index % 2 == 0:
        doubled_numbers = int(number) * 2     #if it is then we know we double the number for luhns algorithm 

        if doubled_numbers > 9:
            doubled_numbers = doubled_numbers - 9    #if the number is larger by subtracting 9 we are following luhns algorithm this way is just easier as 11-9=2 and 1+1 = 2

        changed_numbers.append(doubled_numbers)
    else:
        changed_numbers.append(int(number))     #these add the changed numbers back to the list 

total_sum = int(check_number) + sum(changed_numbers)    # this the second to last step following luhns algorithm and is adding our check number to the sum of the changed numbers

if total_sum % 10 == 0:
    print("This credit card number is valid")         #if sum is divisable by 10 we know that the crad number is valid according to luhns algorithm 
else:
    print("This credit card number is not valid")
