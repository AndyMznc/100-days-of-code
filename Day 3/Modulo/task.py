# Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".

number = int(input("S'il vous plait, choisissez un nombre: "))

if number % 2 == 0:
    print("Ce chiffre est pair")
else:
    print("Ce chiffre est impair")
