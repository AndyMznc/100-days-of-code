import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# print(random.choice(letters))

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Correction
# Easy
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(password)

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

# # Hard
# count_letters = 0
# count_symbols = 0
# count_numbers = 0
# array_password = []

# for letter in letters:
#     if count_letters < nr_letters:
#         array_password += random.choices(letters)
#         count_letters += 1

# for symbol in symbols:
#     if count_symbols < nr_symbols:
#         array_password += random.choices(symbols)
#         count_symbols += 1

# for number in numbers:
#     if count_numbers < nr_numbers:
#         array_password += random.choices(numbers)
#         count_numbers += 1

# random.shuffle(array_password)
# password = "".join(str(letter) for letter in array_password)
# print(password)

# # Easy
# password = ""
# count_letters = 0
# count_symbols = 0
# count_numbers = 0

# for letter in letters:
#     if count_letters < nr_letters:
#         password += random.choice(letters)
#         count_letters += 1

# for number in numbers:
#     if count_numbers < nr_numbers:
#         password += random.choice(numbers)
#         count_numbers += 1

# for symbol in symbols:
#     if count_symbols < nr_symbols:
#         password += random.choice(symbol)
#         count_symbols += 1

# print(password)
