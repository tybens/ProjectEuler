# PROBLEM 5 (NOT BRUTE-FORCE !!!) - (09/03)
import math
# Prime factorization, each number [1-20] can be made through a subset of multiplication of
# these prime factors. 1 = 1, 2 = 2, 3 = 3, 4 = 2*2, 5=5, 6=3*2, 
# print(1*2*2*2*2*3*3*5*7*11*13*17*19) 
def primeFactors(n): 
    ret = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        ret.append(2), 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3, int(math.sqrt(n))+1, 2): 
          
        # while i divides n, print i ad divide n 
        while n % i == 0: 
            ret.append(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        ret.append(n)
        
    return ret

even_division_all_numbers_below = 21
ret = [1]
toextend = []

for num in range(1, even_division_all_numbers_below):
    for fac in primeFactors(num):
        # print("primeFactors(num): " + str(primeFactors(num)))
        already = True
        for i, already_in in enumerate(ret):
            if fac == already_in and already:
                already = False
                # print("num: " + str(num) + " fac: " + str(fac) + " ret: " + str(ret) + " del ret[i]: " + str(ret[i]))
                del ret[i]
        
        toextend.append(fac)
    ret.extend(toextend)
    # print("RET: " + str(ret))
    toextend = []
    

    
result=1
for i in ret:
    result = i*result
print(result)
