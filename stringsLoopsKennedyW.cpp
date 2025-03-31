#include <iostream>
#include <string>

using namespace std;


// Kennedy Watson
// SCIS 123
// Strings and loops lab


int main() {


// Make loop in case user wants to continue program

char exit;

do{

    // Initialize the input variable
    string word;

    // Prompt the user and get word/input
    cout << "Enter a string: ";
    getline(cin, word);

    // 1 - Print only uppercase letters
    cout << "Condition 1: ";
    for (size_t k = 0; k < word.length(); k++) { 
        if (word[k] >= 'A' && word[k] <= 'Z') {  // This is to check and see if the character is uppercase
            cout << word[k];
        }
    }
    cout << endl;

    // 2 - Print every second letter
    cout << "Condition 2: ";
    for (size_t k = 0; k < word.length(); k += 2) { // This is gonna skip every other letter
        cout << word[k];
    }
    cout << endl;

    // 3 -  Replace the vowels with underscores
    cout << "Condition 3: ";
    for (size_t k = 0; k < word.length(); k++) {
        if (word[k] == 'a' || word[k] == 'e' || word[k] == 'i' || word[k] == 'o' || word[k] == 'u' ||
            word[k] == 'A' || word[k] == 'E' || word[k] == 'I' || word[k] == 'O' || word[k] == 'U') {
            cout << "_";
        } else {
            cout << word[k];
        }
    }
    cout << endl;

    // 4 - Print positions of vowels
    cout << "Condition 4: " << endl;
    for (size_t k = 0; k < word.length(); k++) {
        char character = word[k];
        if (character == 'a' || character == 'e' || character == 'i' || character == 'o' || character == 'u' ||
            character == 'A' || character == 'E' || character == 'I' || character == 'O' || character == 'U') {
            cout << k << " " << endl;
        }
    }
        cout << endl;

     cout << "Would you like to continue this program? (Y/y)" << endl;
     cin >> exit;
     cin.get();  // Reads new line character

}
while(exit == 'Y' || exit == 'y');

    return 0;
}

