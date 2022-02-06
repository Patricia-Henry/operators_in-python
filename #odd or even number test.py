#odd or even number test
number = int(input("Which number do you want to check? "))



new_number = int(number % 2)
if new_number == 0:
    print("that is an even number")
else:
    print("that is an odd number")