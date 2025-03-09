true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]

letters_from_names = []


def calculate_love_score(name1, name2):
    letters_from_names = list(name1 + name2)
    count_word_true = 0
    count_word_love = 0

    for letter in letters_from_names:
        for letter_in_true in true:
            if letter == letter_in_true:
                count_word_true += 1

        for letter_in_love in love:
            if letter == letter_in_love:
                count_word_love += 1

    love_score = int(str(count_word_true) + str(count_word_love))
    print(love_score)


calculate_love_score("Angela Yu", "Jack Bauer")
