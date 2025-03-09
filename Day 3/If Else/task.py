print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you ?"))
    if age >= 18:
        print("You're ticket will cost 12$")
    else:
        print("You're ticket will cost 7$")
else:
    print("Sorry, you have to grow taller before you can ride.")
