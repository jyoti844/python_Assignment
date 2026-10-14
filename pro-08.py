
def calculate_grades(*args, **kwargs):
    marks = args

    minimum = min(marks)
    maximum = max(marks)
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print("Student Name:", kwargs.get("name", "Unknown"))
    print("Marks:", marks)
    print("Minimum Marks:", minimum)
    print("Maximum Marks:", maximum)
    print("Average Marks:", average)
    print("Final Grade:", grade)

    return minimum, maximum, average, grade


# Function call
result = calculate_grades(85, 90, 78, 92, name="Rahul")

# Tuple unpacking
minimum, maximum, average, grade = result

print("\nUnpacked Results:")
print(minimum, maximum, average, grade)
