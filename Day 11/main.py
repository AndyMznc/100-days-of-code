import random

import art


def handle_ace(hand):
    ace = 11
    if hand and hand[-1] == ace:
        if sum(hand) > 21:
            hand[-1] = 1


def draw_card(hand):
    hand.append(random.choice(cards))
    handle_ace(hand)


def result(user_hand, computer_hand):
    user_hand_value = sum(user_hand)
    computer_hand_value = sum(computer_hand)

    print(f"Your final hand: {user_hand}, final score: {sum(user_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")

    if user_hand_value > 21:
        print("You went over. You lose 😭")
    elif computer_hand_value > 21:
        print("Opponent went over. You win 😁")
    elif user_hand_value == computer_hand_value:
        print("Draw 🙃")
    elif user_hand_value > computer_hand_value:
        print("You win 😃")
    elif user_hand_value < computer_hand_value:
        print("You lose 😤")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = {10, 11}
user_hand = []
computer_hand = []


want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if want_play == "y":
    print(art.logo)
    user_hand = random.sample(cards, 2)
    computer_hand = random.sample(cards, 2)

    if blackjack.issubset(set(computer_hand)):
        print("Lose, opponent has Blackjack 😱")
        print(computer_hand)
    elif blackjack.issubset(set(user_hand)):
        print("Win with a Blackjack 😎")
        print(user_hand)

    else:
        print(f"    Your cards: {user_hand}, current score: {sum(user_hand)}")
        print(f"    Computer's first card: {computer_hand[0]}")

        while sum(user_hand) < 21 and sum(computer_hand) < 16:
            continue_draw = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            if continue_draw == "y":
                draw_card(user_hand)

            if continue_draw == "n":
                while sum(computer_hand) < 16:
                    draw_card(computer_hand)

            print(f"    Your cards: {user_hand}, current score: {sum(user_hand)}")
            print(f"    Computer's first card: {computer_hand[0]}")

        result(user_hand, computer_hand)

elif want_play != "n":  # NOTE : Placeholder in case wrong input is enter.
    print("    Your final hand: [10,10], final score: 20")
    print("    Computer's final hand: [4,11,5], final score: 20")
    print("Draw 🙃")
