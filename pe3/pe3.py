# PROBLEM 3 - (09/03)

def isprime(num):
    upto = num**(1/2)    
    if num==1:
        return False
    for i in range(2, round(upto)+1):
        if num % i == 0:
            return False
    return True

bignum = 600851475143
ret = 0

for i in range(2, round(bignum/2)):
    if bignum % i == 0:
        if isprime(int(bignum/i)):
            ret = bignum/i
            break
        
print(ret)
    


