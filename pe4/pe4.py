# PROBLEM 4 - (09/03)
import math


def check_palindrome_of_number(number):
    a = str(number)
    for i in range(math.floor(len(a)/2)):
        if a[i] != a[len(a)-i-1]:
            return False
    return True
    
num1 = 999
num2 = 999
increment2 = True
save = 0
check = 10000000

for i in range(100, 999):
    while(increment2 and (check >= save)):
        check = num1*num2
        # print("num1: " + str(num1) + " num2: " + str(num2) + " product: " + str(check))

        if check_palindrome_of_number(check):      
            snum1 = num1
            snum2 = num2
            save = check
            increment2 = False # break out of increment2 while loop
        num2-=1
    num1-=1
    num2=999
    check = num1*num2
    if check < save:
        break
    increment2=True
    
print("num1: " + str(snum1) + "\nnum2: " + str(snum2) + "\nproduct: " + str(save))
            
