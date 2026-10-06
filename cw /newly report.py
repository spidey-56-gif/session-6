NUM_SCORES = 3

students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def total_score(record):
    total = 0
    for i in range(1, len(record)):
        total = total + record[i]
    return total


def average_score(record):
    return total_score(record) / NUM_SCORES


print("REPORT")

for student in students:
    total = total_score(student)
    average = average_score(student)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{student[0]} {total} {average}{grade}")

class_average_sum = 0
for student in students:
    class_average_sum = class_average_sum + average_score(student)

print(f"Classaverage:{class_average_sum / len(students)}")

highest_average = 0
topper_name = ""
for student in students:
    average = average_score(student)
    if average > highest_average:
        highest_average = average
        topper_name = student[0]
print(f"Topper: {topper_name}{highest_average}")
