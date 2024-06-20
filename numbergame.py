import random

def yokesh_game():
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0
    guess = None

    print("Welcome to Yokesh's Number Guessing Game!")
    print("Yokesh has selected a number between 1 and 100.")
    print("Can you guess what it is?")

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            number_of_guesses += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! Yokesh congratulates you for guessing the number in {number_of_guesses} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    yokesh_game()
