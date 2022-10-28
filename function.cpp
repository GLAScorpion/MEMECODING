using namespace Rational;
rational operator+(rational op1, rational op2){
    int nres = op1.get_num*op2.get_den+op1.get_den*op2.get_num;
    rational result = rational(nres,com_multi(op1,op2));
    return result;
}
int com_multi(rational& op1, rational& op2){
    return op1.get_den() * op2.get_den();
}
rational operator+(rational op1, int op2){
    rational result = rational(op1.get_den * op2 + op1.get_num,op1.get_den);
    return result;
}
rational operator-(rational op1, rational op2){
    int nres = op1.get_num*op2.get_den-op1.get_den*op2.get_num;
    rational result = rational(nres,com_multi(op1,op2));
    return result;
}
rational operator*(rational op1, rational op2);
rational operator/(rational op1, rational op2);
std::ostream& operator<<(std::ostream&);
rational::double to_double(rational op){
    return std::static_cast<double>op.get_num/op.get_den;
bool operator==(rational op1, rational op2){
    if(op1.get_num==op2.get_num and op2.get_den==op1.get_den){
        return true;
    }
    return false;
}
bool operator>(rational op1, rational op2);
bool operator<(rational op1, rational op2);
}
//member functions
rational::class Invalid{
    public:
    Invalid(){
        throw std::illegal_argument("Invalid denominator");
    }
}
rational::rational(){
}
rational::rational(int num){
    numerator = num;
}
rational::rational(int num, int den){
    if (den == 0){
        throw Invalid();
    }
    numerator = num;
    denominator = den;
}
rational::void operator=(rational op){
    this.denominator = op.denominator;
    this.numerator = op.denominator;
}


