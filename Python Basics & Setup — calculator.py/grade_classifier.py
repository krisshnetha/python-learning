marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks entered")
else:
    if marks >= 90:
        grade = "A"
        message = "Excellent work!"
    elif marks >= 75:
        grade = "B"
        message = "Great job!"
    elif marks >= 60:
        grade = "C"
        message = "Good effort!"
    elif marks >= 40:
        grade = "D"
        message = "You passed. Keep improving!"
    else:
        grade = "F"
        message = "Don't give up. Practice more!"

    status = "Pass" if marks >= 40 else "Fail"

    print(f"Grade: {grade}")
    print(f"Status: {status}")
    print(message)