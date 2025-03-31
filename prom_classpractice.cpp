#include <iostream>
#include <string>
using namespace std;
// Kennedy Watson
// Prom Program 
int main() {
   string outfit, gender;
   int height;

   // Prompt user for what type of outfit they want
   cout << "Would you like a tuxedo or dress?" << endl;
   cin >> outfit;

   // Prompt user for gender
   cout << "Are you male or female?" << endl;
   cin >> gender;

   // If user is male
   if (gender == "male") {
      // Get height of the user
      cout << "Enter your height in inches:" << endl;
      cin >> height;

      // Recommend a tuxedo based on height
      if (height < 55) {
         cout << "You need a short tuxedo." << endl;
      } else if (height >= 55 && height <= 60) {
         cout << "You need a medium tuxedo." << endl;
      } else {
         cout << "You need a tall tuxedo." << endl;
      }

      // Recommend opposite outfit (dress)
      if (height < 55) {
         cout << "You need a petite dress." << endl;
      } else if (height >= 55 && height <= 60) {
         cout << "You need a medium dress." << endl;
      } else {
         cout << "You need a tall dress." << endl;
      }

   } 
   // If user is female
   else if (gender == "female") {
      // Get height of the user
      cout << "Enter your height in inches:" << endl;
      cin >> height;

      // Recommend a dress based on height
      if (height < 55) {
         cout << "You need a petite dress." << endl;
      } else if (height >= 55 && height <= 60) {
         cout << "You need a medium dress." << endl;
      } else {
         cout << "You need a tall dress." << endl;
      }

      // Recommend the opposite outfit (tuxedo)
      if (height < 55) {
         cout << "You need a short tuxedo." << endl;
      } else if (height >= 55 && height <= 60) {
         cout << "You need a medium tuxedo." << endl;
      } else {
         cout << "You need a tall tuxedo." << endl;
      }

   } 
   // If an invalid gender input is entered
   else {
      cout << "Invalid input for gender!" << endl;
   }

   return 0;
}

