students_test_score = int(input())
max_test_score = int(input())

students_percentile = (students_test_score / max_test_score) * 100

if students_percentile >= 90:
    students_grade = "A"
elif students_percentile >= 80:
    students_grade = "B"
elif students_percentile >= 70:
    students_grade = "C"
elif students_percentile >= 60:
    students_grade = "D"
else:
    students_grade = "F"
    
print(students_grade)
