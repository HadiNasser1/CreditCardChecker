cardNo = list("4388576018402626")

check_number = cardNo.pop()
cardNo.reverse()

changed_numbers = []

for index, number in enumerate(cardNo):
    if index % 2 == 0:
        doubled_numbers = int(number) * 2

        if doubled_numbers > 9:
            doubled_numbers = doubled_numbers - 9

        changed_numbers.append(doubled_numbers)
    else:
        changed_numbers.append(int(number))

total_sum = int(check_number) + sum(changed_numbers)

if total_sum % 10 == 0:
    print("This credit card number is valid")
else:
    print("This credit card number is not valid")
