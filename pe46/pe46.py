# PROBLEM 46 - (09/20)
    # Goldbach's other conjecture
        # odd composites can be written as the sum of a prime and twice a square


def isprime(num):
    upto = num**(1/2)    
    if num==1:
        return False
    for i in range(2, round(upto)+1):
        if num % i == 0:
            return False
    return True


def conjecture(prime_num):
    i = 0
    ret = prime_num
    while True:
        yield prime_num + 2 * (i ** 2)
        i+=1
        
squares_upto = 10000
check_primes_upto = 20000
works = set()

for i in range(1, check_primes_upto, 2):
    if isprime(i):
        it = conjecture(i)
        for j in range(1, squares_upto + 1):
            works.add(next(it))
            
            
            
i = 1
while True:
    i += 2
    if not isprime(i):
        if i not in works:
            print(i)
            break
