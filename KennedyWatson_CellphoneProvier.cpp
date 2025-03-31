// Kennedy Watson
// Program that will compute the monthly cell phone charge

#include <iostream>
#include <iomanip> // For the setprecision function

using namespace std;

/*
Monthly cell phone charge

1 Define the constants with const
   - BASE_CHARGE = 29.95 (This is the monthly charge for up to 300)
   - BASE_MINUTES = 300 (These are the included minutes in the base charge)
   - EXTRA_MINUTE_COST = 0.45 (This is going to be the charge for each additional minute)
   - TAX_RATE = 12.5% (Tax applied to the total charge)

2 Declare variables:
   - minutes_used (Integer stores user input for minutes used)
   - extra_charge (Double stores the additional charge for extra minutes)
   - total_charge (Double to store total cost before tax)
   - tax (Double for computed tax amount)
   - final_charge (Double that stores the total final charge including tax)


3 Prompt user for input:
Prompt will display message: "Enter the number of minutes used: " Then, the program will read the user input and store it in minutes_used

4 Calculate extra charge:
   - If minutes_used is greater than BASE_MINUTES, = extra_minutes = minutes_used - BASE_MINUTES. Then, extra_charge = extra_minutes * EXTRA_MINUTE_COST
   Else statement will be extra_charge = 0

5 Total charges
   - total_charge = BASE_CHARGE + extra_charge
   - tax = total_charge * TAX_RATE
   - final_charge = total_charge + tax

6 Display the output:
   - Format the output in a way that will display two decimal places, with setprecison
   - Display the message: "Your total monthly charge is: $ final_charge

7 End program with return 0
*/

int main() {
    const double BASE_CHARGE = 29.95;
    const int BASE_MINUTES = 300;
    const double EXTRA_MINUTE_COST = 0.45;
    const double TAX_RATE = 0.125;
    
    int minutes_used;
    double total_charge, extra_charge = 0.0, tax, final_charge;
    
// This part is the user input
    cout << "Enter the number of minutes used: ";
    cin >> minutes_used;
    
    if (minutes_used > BASE_MINUTES) 
    {
        int extra_minutes = minutes_used - BASE_MINUTES;
        extra_charge = extra_minutes * EXTRA_MINUTE_COST;
    }
    
    total_charge = BASE_CHARGE + extra_charge;
    tax = total_charge * TAX_RATE;
    final_charge = total_charge + tax;
    
// setprecision for two decimal points 
    cout << fixed << setprecision(2);
    cout << "Your total monthly charge is: $" << final_charge << endl;
    
    return 0;
}
