MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# TODO: Calculate the monetary inserted.
def calculate_monetary(quarters, dimes, nickles, pennies):
    amount_inserted = 0
    amount_inserted += quarters * 0.25
    amount_inserted += dimes * 0.10
    amount_inserted += nickles * 0.05
    amount_inserted += pennies * 0.01

    return amount_inserted


def check_resources(drink, status):
    if drink == "off":
        return is_under_maintenance(status)

    if drink == "report":
        return report_data()

    enough_resources = True
    drink_ingredient = MENU[drink]["ingredients"]

    for ingredient_needed in drink_ingredient:
        quantity_needed = drink_ingredient[ingredient_needed]

        for ingredient_in_stock in resources:
            quantity_in_stock = resources[ingredient_in_stock]

            if ingredient_needed == ingredient_in_stock:
                if quantity_needed > quantity_in_stock:
                    enough_resources = False
                    print("Sorry there is not enough [...]")

    return enough_resources


def is_under_maintenance(status):
    # global in_maintenance
    status = True
    return


def report_data():
    for resource in resources:
        if resource == "milk" or resource == "water":
            print(f"{resource.title()}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.title()}: {resources[resource]}g")
        elif resource == "money":
            print(f"{resource.title()}: ${resources[resource]}")


def payment_verification(currency_introduced, drink_price):
    currency_returned = 0
    if currency_introduced > drink_price:
        currency_returned = round(currency_introduced - drink_price, 2)
        resources["money"] = drink_price

        print(f"Here is ${currency_returned} in change.")
        print("Here is your latte ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def machine_coffee():
    in_maintenance = False
    chosen_drink = ""
    while not in_maintenance:
        # TODO: When typing "off" anywhere, stop the program
        if chosen_drink == "off":
            in_maintenance = True
            return

        # TODO: Ask the user what he want, and store the value.
        chosen_drink = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower()

        # TODO: When typing "report", display the current ressources

        # TODO: When ordering a drink, check if the machine has enough ressources to make it
        check_resources(chosen_drink, in_maintenance)

        # TODO: - If, not enough ressources, stop the process and inform the user about it.

        # TODO: If enough ressource to make the drink, then prompt user to pay.

        # TODO: Ask user to insert coins.
        print("Please insert coins.")
        inserted_quarters = int(input("how many quarters?: "))
        inserted_dimes = int(input("how many dimes?: "))
        inserted_nickles = int(input("how many nickles?: "))
        inserted_pennies = int(input("how many pennies?: "))

        currency_introduced = calculate_monetary(
            quarters=inserted_quarters,
            dimes=inserted_dimes,
            nickles=inserted_nickles,
            pennies=inserted_pennies,
        )

        # TODO: Verify if the user insert enough money to pay the drink.
        chosen_drink_price = MENU[chosen_drink]["cost"]
        payment_verification(currency_introduced, chosen_drink_price)

        # TODO: If not enough money, do not add the money to the "ressources" and refund the user.

        # TODO: If enough money inserted, add the money to the "ressources"

        # TODO: If the user has inserted too much money, the machine should give change. And inform the user how much

        # TODO: If the transaction is successful, deducted the ressources needed to the machine.

        # TODO: Give the coffee to the user ☕

        # TODO: Loop everything


machine_coffee()
