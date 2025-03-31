#include <iostream>
using namespace std;

// Kennedy Watson
// SCIS 123
// Calculator program that takes user input and prints out result, also verifies/validates user input


int main() {
    char operation;
    double num1, num2;

    cout << "Simple Calculator" << endl;
    cout << "Choose an operation (+, -, *, /): ";
    cin >> operation;

    // Validate operation input
    if (operation != '+' && operation != '-' && operation != '*' && operation != '/') {
        cout << "Error: Invalid operation. Please enter +, -, *, or /." << endl;
        return 1;
    }

    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    // Check for division by zero
    if (operation == '/' && num2 == 0) {
        cout << "Error: Division by zero is not allowed." << endl;
        return 1;
    }

    switch (operation) {
        case '+':
            cout << "Result: " << num1 << " + " << num2 << " = " << (num1 + num2) << endl;
            break;
        case '-':
            cout << "Result: " << num1 << " - " << num2 << " = " << (num1 - num2) << endl;
            break;
        case '*':
            cout << "Result: " << num1 << " * " << num2 << " = " << (num1 * num2) << endl;
            break;
        case '/':
            cout << "Result: " << num1 << " / " << num2 << " = " << (num1 / num2) << endl;
            break;
    }

    return 0;
}
