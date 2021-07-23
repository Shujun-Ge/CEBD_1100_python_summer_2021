# Multiples of Ten:
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

while True:
    number = input("Please enter a whole number : ")
    if number.upper() == "Q":
        break

    number = int(number)

    if number % 10 == 0:
        # pass
        print("Number is a multiple of 10")
    else:
        print("Number is Not a multiple of 10")

