# create an algorithm that reads 4 numbers from the keyboard and prints on the screen whether the sum of the 4 numbers is an even or odd value

info_first_num = int(input("Digit the first number: "))
info_second_num = int(input("Digit the second number: "))
info_third_num = int(input("Digit the third number: "))
info_forth_num = int(input("Digit the forth number: "))

result_sum_info_numbers = info_first_num + info_second_num + info_third_num + info_forth_num

if result_sum_info_numbers % 2 == 0 :
    print("The number result is even: ", result_sum_info_numbers)
else:
    print("The number result is odd: ", result_sum_info_numbers)
