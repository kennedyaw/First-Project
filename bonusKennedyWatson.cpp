// Kennedy Watson
// SCIS 123
#include <iostream>
#include <iomanip> // For formatting prices to be certain places for decimals

using namespace std;

// This program is meant to read user input of a switch statement for a menu item and then will output the price. It validates user input as well, while asking user continuously for their selection until they opt out of the program.



int main() {
    // Initialize variables
    char menuSelection;
    double totalPrice = 0.0;
    int pizzaNum = 0, saladNum = 0, burgerNum = 0;

    // Display menu
    cout << "Welcome to the menu! Here are our choices: " << endl;
    cout << "P - Pizza: $6.99\n";
    cout << "S - Salad: $5.99\n";
    cout << "B - Burger: $7.99\n";
    cout << "Q - Quit\n";

    // Start the while loop to take orders
    while (true) {
        cout << "\nEnter your choice (P: Pizza, S: Salad, B: Burger, Q: Quit): ";
        cin >> menuSelection;
        menuSelection = toupper(menuSelection); // Convert to uppercase just so the inputs are consistent

        // Check for whitespace or empty input
        if (menuSelection == '\n' || menuSelection == ' ') {
            cout << "Error - No value entered" << endl;
            continue; // Restart loop if whitespace or no input
        }

        // Check if input is valid before reading it
        if (menuSelection == 'P' || menuSelection == 'S' || menuSelection == 'B' || menuSelection == 'Q') {
            // If input is valid, you can keep going with the switch statement
        
            // This part will validate and read the user input
            // Start switch statements
            switch (menuSelection) {
                case 'P':
                    cout << "You ordered a pizza, which costs $6.99." << endl;
                    totalPrice += 6.99;
                    pizzaNum++;
                    break;
                case 'S':
                    cout << "You ordered a salad, which costs $5.99." << endl;
                    totalPrice += 5.99;
                    saladNum++;
                    break;
                case 'B':
                    cout << "You ordered a burger, which costs $7.99." << endl;
                    totalPrice += 7.99;
                    burgerNum++;
                    break;
                // This is the quitting option
                case 'Q':
                    cout << "\nThank you for ordering!\n";
                    cout << fixed << setprecision(2); // Make sure that there are two decimal places for prices
                
                    // Start outputting the user's menu selections and their total price
                    // Make sure you account for plural items, use (s)
                    cout << "This is your total price: $" << totalPrice << endl;
                    cout << "Here's what you ordered:" << endl;
                    cout << " * " << pizzaNum << " Pizza(s)\n";
                    cout << " * " << saladNum << " Salad(s)\n";
                    cout << " * " << burgerNum << " Burger(s)\n";
                    return 0; // Exit program
            }
        } else {
            // Invalid input
            cout << "Invalid choice. Please enter P, S, B, or Q.\n";
        }
    }
}
