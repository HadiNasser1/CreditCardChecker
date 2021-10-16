cardNo = list(input("What is your card number:))

# this takes the last number out of the list, making it our check number for later use.
check_number = cardNo.pop()
# reverses the code as it makes it easier for us to use the algorithm
cardNo.reverse()

# We create an empty list to store our new numbers in later on.
changed_numbers = [] 

# We use a for loop here to iterate the sequence and go through each element of list. Enumerate() is used here to make an index of every number in the last, allowing us to run Luhn's algorithm.
for index, number in enumerate(cardNo):
    # Using the condition statement, we check if the index number is even or not. If it is even then we double it.
    if index % 2 == 0:
        doubled_numbers = int(number) * 2 

        # If the number is larger than 9, then we subtract 9 and use the remainder instead.
        if doubled_numbers > 9:
            doubled_numbers = doubled_numbers - 9
                       
        # This changes the empty list by adding the even numbers into it after they were doubled and adding the odd numbers in without any changes.
        changed_numbers.append(doubled_numbers)
    else:
        changed_numbers.append(int(number))

# this the second to last step following luhns algorithm and is adding our check number to the sum of the changed numbers
total_sum = int(check_number) + sum(changed_numbers)   
                
# if sum is divisable by 10 we know that the crad number is valid according to luhns algorithm
if total_sum % 10 == 0:
    print("This credit card number is valid") 
else:
    print("This credit card number is not valid")
