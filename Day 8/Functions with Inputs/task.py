def greet():
    print("Hello!")
    print("How do you do?")
    print("Isn't the weather nice ?")


greet()

print("########################")

#  Function that allows for inputs


def greet_with_name(name="David", location="Quebec"):
    print(f"Hello, my name is {name} !")
    print(f"And i live in {location} ?")


greet_with_name()

user_name = input("What your name ? ")
user_location = input("Where do you live ? ")
greet_with_name(user_name, user_location)


def life_in_weeks(age):
    year_remaining = 90 - age
    week_remaining = year_remaining * 52

    print(f"You have {week_remaining} weeks left.")


life_in_weeks(30)
