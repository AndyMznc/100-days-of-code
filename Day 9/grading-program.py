student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

student_grades = {}
for key in student_scores:
    score = student_scores[key]
    value = ""
    if score >= 91:
        value = "Outstanding"
    elif score >= 81:
        value = "Exceeds Expectations"
    elif score >= 71:
        value = "Acceptable"
    else:
        value = "Fail"

    student_grades[key] = value

print(student_grades)
