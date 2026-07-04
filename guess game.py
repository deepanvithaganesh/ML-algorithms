number = 36
attempts = 0
max_attempts = 10
found = False
print("===== Welcome to the Guessing Game =====")

while not found and attempts < max_attempts:
    attempts += 1
    user_entry = int(input("Enter a number: "))

    if user_entry == number:
        print("Congratulations you won")
        score = (max_attempts - attempts) * 10
        print("Your score:", score)

        break

    elif user_entry > number:
        print("Number is Higher")
        attempts_left = max_attempts - attempts
        print("You have", attempts_left, "attempts left")
    elif user_entry < number:
        print("Number is lower")
        attempts_left = max_attempts - attempts
        print("You have", attempts_left, "attempts left")

else:
    print("You have exhausted all attempts. The number was", number)
    print("Your game is over. You wanna play again?")
