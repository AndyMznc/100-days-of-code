print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
user_input = input('Type "left" or "right" \n')

if user_input.lower() == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    user_input = input('Type "wait" to wait for a boat. Type "swim" to swim across. \n')

    if user_input.lower() == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        user_input = input(
            "  One red, one yellow and one blue. Which colour do you choose? \n"
        )

        if user_input.lower() == "red":
            print("Burned by the fire. Game Over.")
        elif user_input.lower() == "yellow":
            print("You found the treasure! You Win!")
        elif user_input.lower() == "red":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")

    elif user_input.lower() == "swim":
        print("Attacked by trout. Game Over.")
    else:
        print("Wrong input, game cancelled // Game Over.")

elif user_input.lower() == "right":
    print("Attacked by trout. Game Over.")
else:
    print("Wrong input, game cancelled // Game Over.")
