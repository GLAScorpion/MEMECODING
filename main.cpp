#include <iostream>
using namespace std;
namespace Rational(){
    class rational{
    public:
            class Invalid;
            rational();
            rational(int num);
            rational(int num, int den);
            void operator=(rational op);
            int get_num();
            int get_den();
    private:
            int numerator=0;
            int denominator=1;
    }
    int com_multi(rational op1, rational op2);
    double to_double(rational op);
    bool operator==(rational op1, rational op2);
    bool operator>(rational op1, rational op2);
    bool operator<(rational op1, rational op2);
    rational operator+(rational op1, rational op2);
    rational operator+(rational op1, int op2);
    rational operator-(rational op1, rational op2);
    rational operator*(rational op1, rational op2);
    rational operator/(rational op1, rational op2);
    ostream& operator<<(ostream&);
    
}
using namespace Rational;
int main(){
    
}