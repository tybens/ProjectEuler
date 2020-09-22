# PROBLEM 41 - (09/18)
from itertools import permutations   


def isprime(num):
    upto = num**(1/2)    
    if num==1:
        return False
    for i in range(2, round(upto)+1):
        if num % i == 0:
            return False
    return True

# if the sum of the digits of a number is divisible by 3, the digit is divisible by three
summed = 0
for i in range(1, 9+1):
    summed+=i
    if summed % 3 != 0:
        print(i) # 1, 4, 7 (only these up to N pandigitals could be prime)
        

# start with n=7
n = 7
for i in list(permutations(range(n, 0, -1))):
    this_num = int(''.join([str(a) for a in i]))
    if isprime(this_num):
        print(this_num)
        break

# would then go to 4, but we already found the largest one
