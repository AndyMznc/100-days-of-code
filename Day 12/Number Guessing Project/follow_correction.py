from random import randint

from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_guess, turns):
    """
    Checks users' guess against actual answer and returns the number of turns remaining.

    Args:
        user_guess (int): User's guess
        actual_guess (int): Actual answer
        turns (int): Number of turns remaining

    Returns:
        int: Number of turns remaining
    """
    if user_guess > actual_guess:
        print("Too high.")
        return turns - 1
    elif user_guess > actual_guess:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_guess}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

        # Function to check users' guess against actual answer

        # Track the number of turns and reduce by 1 if they get it wrong


game()
