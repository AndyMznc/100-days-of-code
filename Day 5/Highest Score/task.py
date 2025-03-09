student_scores = [
    150,
    142,
    185,
    120,
    171,
    184,
    149,
    24,
    59,
    68,
    199,
    78,
    65,
    89,
    86,
    55,
    91,
    64,
    89,
]


total = 0
for number in range(1, 101):
    total += number
print(total)

# print(sum(student_scores))

sum = 0
for score in student_scores:
    sum += score
print(sum)

# print(max(student_scores))

highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print(highest)
