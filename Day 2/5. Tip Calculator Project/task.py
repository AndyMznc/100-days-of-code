# # We're going to build a tip calculator.
# # If the bill was $150.00, split between 5 people, with 12% tip.
# # Each person should pay:
# # (150.00 / 5) * 1.12 = 33.6
# # After formatting the result to 2 decimal places = 33.60

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

# price_par_person = bill / people
# print(price_par_person)

# tip_value = 1 + (tip / 100)
# print(tip_value)

# # total = round(price_par_person * tip_value, 2)
# # print(total)

# total = price_par_person * tip_value
# formatted_total = f"{total:.2f}"  # Formatage avec 2 décimales
# print(formatted_total)


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tips_as_percent = tip / 100
total_tip_amont = bill * tips_as_percent
total_bill = bill + total_tip_amont
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount:.2f}")
