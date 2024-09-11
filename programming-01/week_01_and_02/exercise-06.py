# For each situation below, write a piece of code to prompt the user to enter such data and have it stored in memory in the correct form (in relation to the data type):
#
# ask for the user's name
# ask for the user's age
# ask for the user's weight

info_name_data = input("Digit your name: ")
info_age_data = int(input("Digit your age: "))
info_weight_data = float(input("Digit your weight: "))

print(f"Value digitated is {info_name_data} ans his type is {type(info_name_data)}.")
print(f"Value digitated is {info_age_data} ans his type is {type(info_age_data)}.")
print(f"Value digitated is {info_weight_data} ans his type is {type(info_weight_data)}.")
