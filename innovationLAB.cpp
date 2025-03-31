#include <iostream>
#include <string>
using namespace std;

int main () {
string myLight;

cout << "Is your light on?" << endl;
cin >> myLight;

if (myLight == "Yes")
    cout << "Your light is on!";


else {
    cout << "Your light is not on! You should probably go flip the switch. :)" << endl;
}

return 0;
}