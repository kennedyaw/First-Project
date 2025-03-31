#include <iostream>
using namespace std;
// Kennedy Watson
// SCIS 123
// This program is a while, for, and do while loop that prints a multiplication table of a number
// prompt user for a number and then print the multiplication number for that table

int main() {
    int num;
    cout << "Enter a number: " << endl;
    cin >> num;

    // While loop with i
    cout << "Multiplication table of " << num << " with a while loop:" << endl;
    int i = 0;
    while (i <= 10) {
        cout << num << " x " << i << " = " << num * i << endl; // x for multiplication sign
        i++;
    }

    // For loop with n
    cout << "Multiplication table of " << num << " with a for loop:" << endl;
    for (int n = 0; n <= 10; n++) {
        cout << num << " x " << n << " = " << num * n << endl;
    }

    // Do-while loop with k
    cout << "Multiplication table of " << num << " with a do-while loop:" << endl;
    int k = 0;
    do {
        cout << num << " x " << k << " = " << num * k << endl;
        k++;
    } while (k <= 10);


return 0; }
