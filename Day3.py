# Taking input for marks in three subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

# Calculate the average marks
average_marks = (subject1 + subject2 + subject3) / 3

# Determine the grade based on average marks
if average_marks >= 90:
    print("Grade: A")
elif 80 <= average_marks < 90:
    print("Grade: B")
elif 70 <= average_marks < 80:
    print("Grade: C")
else:
    print("Grade: Fail")
