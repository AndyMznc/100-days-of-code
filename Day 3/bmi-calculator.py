weight = 1
height = 1.85

bmi = weight / (height**2)

# 🚨 Do not modify the values above
# Write your code below 👇

print(bmi)


# If the bmi is under 18.5 (not including), print out "underweight"
if bmi < 18.5:
    print("underweight")
# If the bmi is 25 (including) or over, print out "overweight"
elif bmi >= 25:
    print("overweight")
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
else:
    print("normal weight")
