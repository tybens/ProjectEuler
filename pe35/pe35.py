# PROBLEM 35 - (09/14)
    # brute-force

import time
start_time = time.clock_gettime_ns(0)

def isprime(num):
    upto = num**(1/2)    
    if num==1:
        return False
    for i in range(2, round(upto)+1):
        if num % i == 0:
            return False
    return True

def circulate(prime):
    perms = list(permutations(str(prime)))
    rotations = [int(''.join(i[:])) for i in perms]
    for rotated in rotations:
        if not isprime(rotated):
            return False
    return True

primes = []
for i in range(1, 1000000, 2):
    if isprime(i):
        primes.append(i)
        
from itertools import permutations

circular_primes = []
for prime in primes:
    if circulate(prime):
        circular_primes.append(prime)

print(circular_primes)
print("How many circular primes are there below one million? -> " + str(len(circular_primes)))
    

end_time = time.clock_gettime_ns(0)
print("The solution took {} s".format((end_time-start_time)*1e-9))
