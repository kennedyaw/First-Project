# Kennedy Watson
# SCIS 111
# Grades/elf

"""
Make if statement
>= is greater than or equal to
Create program that gives letter grade based on number grade inputed by user
If not a certain group of numbers, youll have an F in the class
"""


grade = float(input("What's your grade in the class?"))

if(grade >= 90):
    print("You have an A in the class.")
elif(grade >= 80):
    print("You have a B in the class.")
elif(grade >= 70):
    print("You have a C in the class.")
elif(grade >= 60):
    print("You have a D in the class.")
else:
    print("You have an F in the class.")
