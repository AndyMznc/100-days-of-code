import random

from game_data import data


def compare_most_followers(answer_a, answer_b):
    if answer_a["follower_count"] > answer_b["follower_count"]:
        print(answer_a["follower_count"])
        return answer_a
    else:
        print(answer_b["follower_count"])
        return answer_b


def compare_result(game_status, user_answer, correct_answer):
    if user_answer == correct_answer:
        return "+1 pt"
    else:
        game_status = True
        return game_status


game_over = False
while not game_over:
    # Générer mes deux propositions (A et B)
    answer_a, answer_b = random.sample(data, 2)

    # Afficher les deux proposition en format f-string
    print(
        f"Compare A: {answer_a['name']}, a {answer_a['description']}, from {answer_a['country']}"
    )
    print(
        f"Against B: {answer_b['name']}, a {answer_b['description']}, from {answer_b['country']}"
    )

    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

    user_answer = ""
    if user_input == "A":
        user_answer = answer_a
    else:
        user_answer = answer_b

    score = 0

    correct_answer = compare_most_followers(answer_a, answer_b)
    game_over = compare_result(game_over, user_answer, correct_answer)
    print(game_over)
