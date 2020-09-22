# PROBLEM 37 - (09/15)

primes = [3, 5, 7]

def isprime(num):
    upto = num**(1/2)    
    if num==1:
        return False
    for i in range(2, round(upto)+1):
        if num % i == 0:
            return False
    return True

def untruncate_right(num):
    num = str(num)
    ret = set()
    for i in range(1, len(num)):
        if not isprime(int(num[:-i])):
            ret.add(False)
    if False in ret:
        return False
    return True

def untruncate_left(num):
    num = str(num)
    ret = set()
    for i in range(1, len(num)):
        if not isprime(int(num[i:])):
            ret.add(False)
    if False in ret:
        return False
    return True
    
# digustingly dumb brute-force

i = 7
count = 0
truncatable = []
while count < 11:
    i+=2
    if isprime(i):
        if untruncate_right(i) and untruncate_left(i):
            truncatable.append(i)
            count+=1
print(len(truncatable))
print(sum(truncatable))
