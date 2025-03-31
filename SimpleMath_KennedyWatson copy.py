# Kennedy Watson
# SCIS 111/113
# Simple Math Program


"""
1. print user instructions
2. prompt user to enter 8 numbers
3. define variables
4. add firstc two variables
5. print results
6. repeat instructions for subtraction, multiplication, and division
"""

print("Today, you will enter 8 numbers and I will add, subtract, multiply, and divide them.")
number1 = float(input("What's the first number you'd like to add?"))
number2 = float(input("What's the second number you'd like to add?"))

number3 = float(input("What's the first number you'd like to subtract?"))
number4 = float(input("What's the second number you'd like to subtract?"))

number5 = float(input("What's the first number you'd like to multiply?"))
number6 = float(input("What's the second number you'd like to multiply?"))

number7 = float(input("What's the first number you'd like to divide?"))
number8 = float(input("What's the second number you'd like to divide?"))

# print/display results

print(f'Math equation 1: {number1} + {number2} = {number1 + number2:.2f}')
print(f'Math equation 2: {number3} - {number4} = {number3 - number4:.2f}')
print(f'Math equation 3: {number5} * {number6} = {number5 * number6:.2f}')
print(f'Math equation 4: {number7} / {number8} = {number7 / number8:.2f}')


