#ifndef BIGINTEGER_H
#define BIGINTEGER_H
#include <iostream>
#include <string>
using namespace std;

class BigInteger
{
    public:
        BigInteger();
        BigInteger(string svalue);

        string toString();

        BigInteger add(BigInteger b);

    protected:

    private:
        string svalue;
};

#endif // BIGINTEGER_H
