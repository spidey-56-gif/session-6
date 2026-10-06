import math
d=[["Rahul",78,88,92],["Priya",65,71,69],["Amit",90,94,85],
["Sneha",55,60,58],["Vikram",82,79,88]]
def f(x):
    t = 0
    for i in range(1,len(x)):
        t=t+x[i]
    return t

NUM_SCORES = 3


def count_students_above_class_average(student_records, class_average):
    """Return how many students have an average above the class average."""
    above_average_count = 0
    for student_record in student_records:
        student_average = f(student_record) / NUM_SCORES
        if student_average > class_average:
            above_average_count = above_average_count + 1
    return above_average_count

print("REPORT")

for i in range(0,len(d)):
    s=f(d[i])
    a=s/3
    if a >= 90:
        g="A"
    elif a>=80:
        g="B"
    elif a>=70:
        g="C"
    elif a>=60:
        g="D"
    else:
        g="F"
    print(d[i][0]+" "+str(s)+" "+str(a)+""+g)

t2=0
for i in range(0,len(d)):
    s=f(d[i])
    a=s/3
    t2=t2+a

class_average = t2 / len(d)
print("Classaverage:"+str(class_average))
students_above_class_average = count_students_above_class_average(d, class_average)
print(f"Students above class average: {students_above_class_average}")

h=0
n=""
for i in range(0,len(d)):
    s=f(d[i])
    a=s/3
    if a>h:
        h=a
        n=d[i][0]
print("Topper: "+n+""+str(h))
