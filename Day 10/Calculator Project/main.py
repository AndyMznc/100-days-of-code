import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


result = 0
current_loop = 0
still_continue = True

number_1 = float(int(input("What's the first number?: ")))
while still_continue:
    current_loop += 1
    operator = input("Pick an operation: ")
    number_2 = float(int(input("What's the next number?: ")))

    if current_loop == 1:
        result = operations[operator](number_1, number_2)
        print(f"{number_1} {operator} {number_2} = {result}")
    else:
        old_value = result
        result = operations[operator](result, number_2)
        print(f"{old_value} {operator} {number_2} = {result}")

    continue_calculating = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
    ).lower()

    if continue_calculating == "n":
        still_continue = False
