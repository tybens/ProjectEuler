# PROBLEM 10 - (09/05)
    # optimization: sieve of eratosthenes
    
def isprime(num):
    upto = num**(1/2)    
    if num==1:
        return False
    for i in range(2, round(upto)+1):
        if num % i == 0:
            return False
    return True

ret = 2 # only checking odd numbers (so I start with 2)
num = 1
while num < 2000000:
    if isprime(num):
        ret+=num
    num+=2 # skip even numbers
    
print(ret)
