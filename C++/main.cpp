#include <iostream>
#include "function.h"
using namespace std;
string print_bool(bool ans){
    if(ans){
        return "True";
    }
    return "False";
}
int main(){
    rational num1 = 10;
    rational num2 = rational(10,3);
    rational num3 = rational(3,5);
    rational num4 = 3;
    rational num5 = num4 = num3;
    cout << "Numeri inizializzati: " << num1 << " " << num2 << " " << num3 << " " << num4 << " " << num5 << endl;
    cout << "Numeri inizializzati(double): " << to_double(num1) << " " << to_double(num2) << " " << to_double(num3) << endl;
    cout << "num1 * num2 : " << num1 * num2 << endl;
    cout << "num1 / num2 : " << num1 / num2 << endl;   
    cout << "num2 / num1 : " << num2 / num1 << endl;  
    cout << "num2 > num1 : " << print_bool(num2 > num1) << endl;  
    cout << "num2 < num1 : " << print_bool(num2 < num1) << endl;  
    cout << "num2 == num1 : " << print_bool(num2 == num1) << endl;  
    cout << "num3 == num4 : " << print_bool(num3 == num4) << endl;  
    cout << "num2 + 2 : " << num2 + 2 << endl;  
    cout << "num2 + num3 : " << num2 + num3 << endl;  
    cout << "num2 - num3 : " << num2 - num3 << endl; 

}