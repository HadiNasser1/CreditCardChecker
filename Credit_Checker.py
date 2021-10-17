'''
This code validates a credit card number based on Luhn's algorithm
'''

# First we ask a user for a card number. We strip the white space to avoid interference with the code.
cardNo = input("What is your card number? ").strip()

# We then find the length of the card number. This is used later to validate if the number of digits is applicable or not.
length = len(cardNo)

# We turn the numbers into a list so we can index it later on for Luhn's algorithm.
cardNo_list = list(cardNo)

# We use an if loop here to check the length of the number entered. If it is lower than 13 digits than it will display an error saying the number is too short.
#If the number is larger than 16 than it will display an error message saying the number is too long
if length < 13:
    print ("This credit card number is not valid. It is too short.")
elif length > 16:
    print ("This credit card number is not valid. It is too long.")
else:

# this takes the last number out of the list, making it our check number for later use.
    check_number = cardNo_list.pop()
# reverses the code as it makes it easier for us to use the algorithm
    cardNo_list.reverse()

# We create an empty list to store our new numbers in later on.
    changed_numbers = [] 

    # We use a for loop here to iterate the sequence and go through each element of list. Enumerate() is used here to make an index of every number in the last, allowing us to run Luhn's algorithm.
    for index, number in enumerate(cardNo_list):
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
        print("This credit card number is valid.") 
    else:
        print("This credit card number is not valid.")
