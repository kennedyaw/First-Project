# Kennedy A Watson
# Grade Program

"""
Algorithm: This porgram calculates a grade using homework, labs, and test
1. Ask user for 6 assignment grades
2. First get 3 homework grades
3. Ask user for 2 lab grades
4. Ask user for the test/exam grade
5. Compute homework average (hw1 + hw2 + hw3)/3
6. Compute lab average (lab1 +lab2)/2
7. The final grade is homeworkAvg *.50 +labAvg *.20 + FinalExam *.30
8. Output results with labels. The numbers are floats formatted to 2 decimal places
"""

# Get 3 homework grades

hw1 = int(input("Enter a homework grade"))
hw2 = int(input("Enter the second homework grade"))
hw3 = int(input("Enter the third homework grade"))

# Get 2 lab grades

lab1 = int(input("Enter a lab grade"))
lab2 = int(input("Enter the second lab grade"))

# Get final exam grade

FinalExam = int(input("Enter the final exam grade"))

# Compute homework average

homeworkAvg = (hw1 + hw2 +hw3)/3

# Compute lab average

labAvg = (lab1 + lab2)/2

# Compute final average

"""
FinalAvg = (homeworkAvg *.50) + (labAvg *.20) + (FinalExam *.30)
"""
homeworkPoints = (homeworkAvg *.50)    # All points combined
labPoints = (labAvg *.20)
examPoints = (FinalExam *.30)

FinalAvg = homeworkPoints + labPoints + examPoints

print(f"homeworkAvg={homeworkPoints:.2f}\nlabAvg={labPoints:.2f}\nFinalExam={examPoints:.2f}\nFinalAvg={FinalAvg:.2f}")
