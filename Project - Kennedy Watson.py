# Kennedy Watson
# SCIS 111-113
# Project 1

def main():
# Welcome user
    print("Welcome to the Hair Salon!")
    
# Display hair menu
    print("\nHair Menu:")
    print("1. Curl Treatment ($50)")
    print("2. Silk Press ($60)")
    print("3. Two-strand Twists ($70)")
    print("4. Wash and Go ($40)")
    print("5. Knotless Boho ($80)")

# Get the hairstyle selection
    hairstyle_choice = int(input("Please select a hairstyle (1-5): "))
    
# Assign the hairstyle cost based on what the user chooses
    if hairstyle_choice == 1:
        hairstyle_cost = 50
    elif hairstyle_choice == 2:
        hairstyle_cost = 60
    elif hairstyle_choice == 3:
        hairstyle_cost = 70
    elif hairstyle_choice == 4:
        hairstyle_cost = 40
    elif hairstyle_choice == 5:
        hairstyle_cost = 80
    else:
        print("Invalid selection. Exiting program.")
        return

# Prompt the user for tip percentage
    tip_percentage = float(input("Enter tip percentage (e.g., 15 for 15%): "))
    
# Calculate tip
    tip = (tip_percentage / 100) * hairstyle_cost
    subtotal = hairstyle_cost
# Calculate final total
    final_total = subtotal + tip

# Display the final bill
    print("\n--- Final Bill ---")
    print(f"Hairstyle Cost: ${hairstyle_cost}")
    print(f"Tip: ${tip:.2f}")
    print(f"Total Amount: ${final_total:.2f}")

# Extra services
    print("Do you want any extra services?")
# Print service menu

    selected_services = []
    print("\nHair Services:")
    print("1.Trim", 15.00, [3, 2]),  # Requires Two-strand Twists or Silk Press
    print("2. Deep conditioning mask ($20.00)")
    print("3. Detangling service ($15.00)")
    print("4. Mint steam treatment ($25.00)",[1, 4],)  # Requires Curl Treatment or Wash and Go
    print("5. A take down service ($35.00)",[5],)  # Requires Knotless Boho
    print("6. Done")

# Get choice
#Loop until user selects "Done"
    while True:
        service_choice = int(input("Please select a service (1-6): "))
        
        if service_choice == 1:
            if hairstyle_choice in [3, 2]:  # Requires Two-strand Twists or Silk Press
                selected_services.append(("Trim", 15.00))
                subtotal += 15.00
                print("You've added: Trim ($15.00)")
            else:
                print("Trim is not available for your selected hairstyle.")
        
        elif service_choice == 2:
            selected_services.append(("Deep conditioning mask", 20.00))
            subtotal += 20.00
            print("You've added: Deep conditioning mask ($20.00)")
        
        elif service_choice == 3:
            selected_services.append(("Detangling service", 15.00))
            subtotal += 15.00
            print("You've added: Detangling service ($15.00)")
        
        elif service_choice == 4:
            if hairstyle_choice in [1, 4]:  # Requires Curl Treatment or Wash and Go
                selected_services.append(("Mint steam treatment", 25.00))
                subtotal += 25.00
                print("You've added: Mint steam treatment ($25.00)")
            else:
                print("Mint steam treatment is not available for your selected hairstyle.")
        
        elif service_choice == 5:
            if hairstyle_choice == 5:  # Requires Knotless Boho
                selected_services.append(("Take down service", 35.00))
                subtotal += 35.00
                print("You've added: Take down service ($35.00)")
            else:
                print("Take down service is not available for your selected hairstyle.")
        
        elif service_choice == 6:
            break  #Using break exits loop
        
        else:
            print("Invalid selection. Please choose again.")

# Calculate the final total 2
    final_total = subtotal + tip
    print("       Your Receipt")
    print("-------------------------------")
    print(f"Hairstyle Cost: ${hairstyle_cost:.2f}")
    
    for service_name, service_cost in selected_services:
        print(f"Extra Service: {service_name} (${service_cost:.2f})")
        
    print(f"Tip: ${tip:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total Amount Due: ${final_total:.2f}")

       





if __name__ == "__main__":
    main()

    
