#create an algorithm that asks the user to enter 10 numbers on the keyboard and, for each number entered, prints on the screen whether the number is positive, negative or zero

for i in range(10):
    info_numb = int(input("Digit a number: "))
    if info_numb > 0:
        print("Positive number!")
    elif info_numb == 0:
        print("Zero!")
    else:
        print("Negative number!")
