from random import randint

number_to_find = randint(0, 100)
remaining_attempts = 5

print("*** Mystery Number Game ***")

# Main loop
while remaining_attempts > 0:
    print(f"You have {remaining_attempts} attempt{'s' if remaining_attempts > 1 else ''} left")

    # User input
    user_choice = input("Guess the number: ")
    if not user_choice.isdigit():
        print("Please enter a valid number.")
        continue

    user_choice = int(user_choice)

    if number_to_find > user_choice:
        print(f"The mystery number is greater than {user_choice}")
    elif number_to_find < user_choice:
        print(f"The mystery number is smaller than {user_choice}")
    else:
        break

    remaining_attempts -= 1

# Win or lose
if remaining_attempts == 0:
    print(f"Game over! The mystery number was {number_to_find}")
else:
    print(f"Congratulations! The mystery number was {number_to_find}!")
    print(f"You found the number in {6 - remaining_attempts} attempt(s).")

print("End of the game.")