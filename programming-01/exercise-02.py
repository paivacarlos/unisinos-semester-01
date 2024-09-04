# create an algorithm that asks for the name and age of two players (one at a time). At the end, print the name of
# the oldest player

player_name_first = input("Please, digit your name: ")
player_age_first = input("Digit your age: ")

print(" ")
print("===//===")
print(" ")

player_name_second = input("Please, digit your name: ")
player_age_second = input("Digit your age: ")

if player_age_first > player_age_second:
    print(f"Oh my gosh, you are the oldest, {player_name_first}")
else:
    print(f"Oh my gosh, you are the oldest, {player_name_second}")

if player_age_first == player_age_second:
    print("My god, you are the same age!")
