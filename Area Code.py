# Kennedy Watson
# SCIS 111-113
# Menu Driven Program

# Display menu options

def calculate_area():
    while True:
        print("Menu Driven Program")
        print("1. Area of Circle")
        print("2. Area of Rectangle")
        print("3. Area of Square")
        print("4. Exit")

# Prompt use for their choice
      
        choice = input("Enter your choice: ")
        
        if choice == '1':
            radius = float(input("Enter radius of Circle: "))
            area_circle = 3.14 * radius ** 2
            print(f"Area of Circle: {area_circle}")

        elif choice == '2':
            length = float(input("Enter length of Rectangle: "))
            width = float(input("Enter width of Rectangle: "))
            area_rectangle = length * width
            print(f"Area of Rectangle: {area_rectangle}")

        elif choice == '3':
            side = float(input("Enter side length of Square: "))
            area_square = side ** 2
            print(f"Area of Square: {area_square}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Please enter the correct choice.")

if __name__ == "__main__":
    calculate_area()
