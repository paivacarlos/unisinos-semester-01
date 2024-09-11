# For the items below, create the requested code:
#
# ask the user for 2 integer values and print on the screen the result of dividing one by the other with 2 decimal places
# ask the user for 2 integer values and print on the screen the result of dividing one by the other with 3 decimal places
# ask the user for 2 integer values and print on the screen the result of dividing one by the other with 4 decimal places

for i in range(3):
    info_first_numb = int(input("Digit a number: "))
    info_second_numb = int(input("Digit a number: "))

    result = info_first_numb / info_second_numb
    print(f"Print value with {i + 2} decimal.")
    print(f"Result: {round(result, i + 2)}")

