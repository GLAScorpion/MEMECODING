#include <iostream>
#include "rational.h"
using namespace std;

string print_bool(bool ans);

int main(){
    rational num1 {10}; // test costruttore con un solo argomento
    rational num2 = rational(10,3);
    rational num3 = rational(3,5);
    rational num4 {3}; // variabile dummy
    rational num5; //test costruttore di default
    rational num6 = num4 = num5; // test operatore = concatenato
    cout << "Numeri inizializzati:\nnum1: " << num1 << "\nnum2: " << num2 << "\nnum3: " << num3 << "\nnum4: " << num4 << "\nnum5: " << num5 << "\nnum6: " << num6 << endl;
    cout << "Primi tre numeri in formato double: " << to_double(num1) << " " << to_double(num2) << " " << to_double(num3) << endl;
    cout << "num1 * num2 : " << num1 * num2 << endl;
    cout << "num1 / num2 : " << num1 / num2 << endl;   
    cout << "num2 / num1 : " << num2 / num1 << endl;  
    cout << "num2 > num1 : " << print_bool(num2 > num1) << endl;  
    cout << "num2 < num1 : " << print_bool(num2 < num1) << endl;  
    cout << "num2 == num1 : " << print_bool(num2 == num1) << endl;  
    cout << "num5 == num6 : " << print_bool(num5 == num6) << endl;  
    cout << "num2 + 2 : " << num2 + 2 << endl;  
    cout << "num2 + num3 : " << num2 + num3 << endl;  
    cout << "num2 - num3 : " << num2 - num3 << endl; 
    cout << "num3 - num2 : " << num3 - num2 << endl; 

}
string print_bool(bool ans){
    if(ans){
        return "True";
    }
    return "False";
}