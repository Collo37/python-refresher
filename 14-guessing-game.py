number_of_guesses = 5
guess_count = 0
game_over = False

secret_number = 5
name = input("What is your name? ")
while not game_over:
    guess = int(input(f"What is the secret number {name}? "))
    if guess == secret_number:
        print("Congratulations. You have gotten the number right!!")
        break

    elif number_of_guesses == 0:
        print("game over!!")
        game_over = True
        break
    else:
        number_of_guesses -= 1
        print(f"Sorry. Try again {number_of_guesses} guesses left")
        continue

