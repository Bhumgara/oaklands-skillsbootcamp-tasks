attendance = input("What is your attendance? ")
assignmentScore = input("Assignment Score: ")
examScore = input("Exam Score: ")
finalMark = (assignmentScore * 0.4) + (examScore * 0.6)

if attendance < 75 and examScore < 40:
    print("Fail")
else:
    if finalMark >= 70:
        print("Distinction")
    elif finalMark >= 60:
        print("Merit")
    elif finalMark >= 40:
        print("Pass")
    else:
        print("Fail")