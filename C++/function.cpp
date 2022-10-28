#include "function.h"
rational operator+(rational op1, rational op2){
    int nres = op1.get_num()*op2.get_den()+op1.get_den()*op2.get_num();
    rational result = rational(nres , com_multi(op1,op2));
    return result;
}
int com_multi(rational& op1, rational& op2){
    return op1.get_den() * op2.get_den();
}
rational operator+(rational op1, int op2){
    rational result = rational(op1.get_den() * op2 + op1.get_num(),op1.get_den());
    return result;
}
rational operator-(rational op1, rational op2){
    int nres = op1.get_num()*op2.get_den()-op1.get_den()*op2.get_num();
    rational result = rational(nres,com_multi(op1,op2));
    return result;
}
rational operator*(rational op1, rational op2){
    rational res = rational(op1.get_num()*op2.get_num(),op1.get_den()*op2.get_den());
    return res;
}
rational operator/(rational op1, rational op2){
    rational res = rational(op1.get_num()*op2.get_den(),op1.get_den()*op2.get_num());
    return res;
}
std::ostream& operator<<(std::ostream& os, rational op){
    if(op.get_den() == 1){
        os << op.get_num();
        return os;
    }
    os << op.get_num() << "/" << op.get_den();
    return os;
}
double to_double(rational op){
    return static_cast<double>((op.get_num()/op.get_den()));
}
bool operator==(rational op1, rational op2){
    if(op1.get_num()*op2.get_den() == op1.get_den()*op2.get_num()){
        return true;
    }
    return false;
}
bool operator>(rational op1, rational op2){
    if(op1.get_num()*op2.get_den() > op1.get_den()*op2.get_num()){
        return true;
    }
    return false;
}
bool operator<(rational op1, rational op2){
    if(op1.get_num()*op2.get_den() < op1.get_den()*op2.get_num()){
        return true;
    }
    return false;
}

//member functions
int rational::get_den(){
    return denominator;
}
int rational::get_num(){
    return numerator;
}
rational::rational(){}
rational::rational(int num){
    numerator = num;
}
rational::rational(int num, int den){
    if (den == 0){
        throw std::invalid_argument("Invalid denominator");
    }
    numerator = num;
    denominator = den;
}
rational rational::operator=(rational op){
    denominator = op.denominator;
    numerator = op.numerator;
    rational ret = rational(op.numerator,op.denominator);
    return ret;
}


