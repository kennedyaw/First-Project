# Kennedy Watson
# SCIS 111-113
# This is a program to demonstrate te math module functions
# Due 10.21.24
# Math Model

"""
Algorithm:
1. put import math
2. use ciel, fabs, sqrt, power, factorial, floor, mod, round, sine
3. for each function get input from the user as appropriate (1 or 2 numbers) 
4. call function, print number(s) used and the output and the name of function used
"""
import math

# Get user inputs
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

# Demonstrate the math functions
# 1. Ceil
ceil_result = math.ceil(num1)
print(f"The ceiling of {num1} is {ceil_result}.")

# 2. Fabs
fabs_result = math.fabs(num1)
print(f"The absolute value of {num1} is {fabs_result}.")

# 3. Sqrt
sqrt_result = math.sqrt(num1)
print(f"The square root of {num1} is {sqrt_result}.")

# 4. Pow
pow_result = math.pow(num1, num2)
print(f"{num1} raised to the power of {num2}  is {pow_result}.")

# 5. Factorial
if num1.is_integer() and num1 >= 0:
    factorial_result = math.factorial(int(num1))
    print(f"The factorial of {int(num1)} is {factorial_result}.")
else:
    print(f"Cannot calculate the factorial of {num1} as it is not a non-negative integer.")

# 6. Floor
floor_result = math.floor(num1)
print(f"The floor of {num1} is {floor_result}.")

# 7. Mod (returns the fractional and integer parts)
modf_result = math.modf(num1)
print(f"The fractional and integer parts of {num1} are {modf_result[0]} and {modf_result[1]}.")

# 8. Round
round_result = round(num1)
print(f"{num1} rounded is {round_result}.")

# 9. Sine (using num1)
sine_result = math.sin(math.radians(num1))  # Convert degrees to radians
print(f"The sine of {num1} degrees is {sine_result}.")
