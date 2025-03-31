#include <iostream>
using namespace std;

// Kennedy Watson
// Switcheroo Project Program A
// This program reads in user input for highway numbers and sees what interstate it's on and what direction it goes in


int main() {
    
    int num_highway;
    
    cout << "Enter highway number: ";
    cin >> num_highway;
    
    if (num_highway < 1 || num_highway > 999 || num_highway == 200) {
        cout << "This is an highway number." << endl;
    } else {

    if (num_highway >= 1 && num_highway <= 99) {
        
        cout << "Interstate " << num_highway << " is a primary highway." << endl;
    }
    
    else if (num_highway >= 100 && num_highway <= 999) {
        
        int primary_highway = num_highway % 100;
    
    if (primary_highway == 0) {
        cout << "Invalid highway number." << endl;
        } 
           
    else {
        
        cout << "Interstate " << num_highway << " is an auxiliary highway, serving the Interstate " << primary_highway << "." << endl;
        }
        
    }
    if (num_highway % 2 == 0) {
        cout << "This runs east/west." << endl;
        
    } else {
        
        cout << "This runs north/south." << endl;
    }
    }

return 0;}
