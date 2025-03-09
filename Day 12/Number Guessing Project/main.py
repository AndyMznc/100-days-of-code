import random


def game():
    global attempts_remaining
    still_running = True
    while still_running:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        current_guess = int(input("Make a guess: "))

        comparison_check = compare(guess=current_guess, attempts=attempts_remaining)
        if comparison_check == 1:
            attempts_remaining -= 1
        elif comparison_check == 0:
            still_running = False  # Game is done.


def compare(guess, attempts):
    if guess == number_to_find:
        print(f"You got it! The answer was {number_to_find}")
        return 0
    elif attempts == 1:
        print("You've run out of guesses, you lose.")
        return 0
    elif guess > number_to_find:
        print("Too high.")
        print("Guess again.")
        return 1
    elif guess < number_to_find:
        print("Too low.")
        print("Guess again.")
        return 1


# Generate a random number
number_to_find = random.randrange(1, 100)

# Initialize the attempts
attempts = {"easy": 10, "hard": 5}

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {number_to_find}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts_remaining = attempts[difficulty]

game()
