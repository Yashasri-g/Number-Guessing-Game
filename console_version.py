import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts_left = 5

    print("Welcome to 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts_left} attempts to guess the number.")

    while attempts_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts_left -= 1

        if guess < number_to_guess:
            print(f"Too low! You have {attempts_left} attempts left.")
        elif guess > number_to_guess:
            print(f"Too high! You have {attempts_left} attempts left.")
        else:
            print("Congratulations! You guessed the number correctly!")
            break

        if attempts_left == 0:
            print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

# Run the console-based game
if __name__ == "__main__":
    guess_the_number()
