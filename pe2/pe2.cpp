#include <iostream>

using namespace std;

int main()
{
    int num1, num2;
    num1 = 1;
    num2 = 2;
    int result = 0;

    while(num2 < 4000000) {

        if(num2 % 2 == 0) {
            result+=num2;
        }

        int oldnum2 = num2;
        num2=num1+num2;
        num1 = oldnum2;


    }

    cout << result << endl;
    return 0;
}
