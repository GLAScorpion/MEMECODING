#include <iostream>
class rational{
public:
        rational();
        rational(int num);
        rational(int num, int den);
        rational operator=(rational op);
        int get_num();
        int get_den();
private:
        int numerator {0};
        int denominator {1};
};

double to_double(rational op);
bool operator==(rational op1, rational op2);
bool operator>(rational op1, rational op2);
bool operator<(rational op1, rational op2);
rational operator+(rational op1, rational op2);
rational operator+(rational op1, int op2);
rational operator-(rational op1, rational op2);
rational operator*(rational op1, rational op2);
rational operator/(rational op1, rational op2);
std::ostream& operator<<(std::ostream& os, rational op);