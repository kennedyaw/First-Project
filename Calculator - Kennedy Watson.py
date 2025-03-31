# Kennedy Watson
# SCIS 111-113
# Calculator program
# This program calculates various mathematical operations

# Welcome user
print("Welcome to the K Calculator!")

# Define operations
def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(num1, num2):
    if num2 == 0:
        return "N/A, cannot divide by zero."
    quotient = num1 / num2
    return quotient

def sqr_root(num1):
    if num1 < 0:
        return "N/A, cannot square root a negative number."
    sqrt = num1 ** 0.5
    return sqrt

def raise_power(num1, num2):
    power = num1 ** num2
    return power

def absolute_value(num1):
    return abs(num1)

choice = 0
while choice != 8: # Loop until user chooses to exit
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponent")
    print("7. Absolute Value")
    print("8. EXIT")

    choice = int(input("Please make your choice for the calculator: "))
# Operations that need two numbers
    if choice in [1, 2, 3, 4,]:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
# Operations
# If statements 
    if choice == 1:
        sum_result = add(num1, num2)
        print(f"Your sum is {sum_result}")
    elif choice == 2:
        difference = subtract(num1, num2)
        print(f"Your difference is {difference}")
    elif choice == 3:
        product = multiply(num1, num2)
        print(f"Your product is {product}")
    elif choice == 4:
        quotient = divide(num1, num2)
        print(f"Your quotient is {quotient}")
    elif choice == 5:
        num1 = float(input("Please enter a number for square root: "))
        root = sqr_root(num1)
        print(f"Your square root is {root}.")
    elif choice == 6:
        num1 = float(input("Please enter the base: "))
        num2 = float(input("Please enter the exponent: "))
        result = raise_power(num1, num2)
        print(f"{num1} raised to the power of {num2} is {result}.")
    elif choice == 7:
        num1 = float(input("Please enter a number: "))
        abs_value = absolute_value(num1)
        print(f"The absolute value is {abs_value}.")
    elif choice == 8: # Exits loop and program
        print("Thank you for using the program!")
        break
    else:
        print("Please enter a valid choice.")
