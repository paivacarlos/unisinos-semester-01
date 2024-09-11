# create an algorithm that requests the user's name and age via keyboard. The algorithm should print one of the following messages on the screen:
# “You are an adult”, when the age entered is greater than or equal to 18
# “You are a teenager”, when the age entered is less than 18 and greater than 13
# “You are a child”, when the age entered is greater than or equal to 0 and less than or equal to 13
# “Invalid age”, when the age entered is less than 0

info_age = int(input("Please digit your age: "))

if info_age >= 18:
    print("You are adult!")
elif 18 > info_age > 13:
    print("You are a teenager!")
elif 0 <= info_age <= 13:
    print("You are a child!")
else:
    print("Invalid age!")
