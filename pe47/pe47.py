# PROBLEM 47 - (09/20)
    # broken
import math
    
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


i = 1
while i < 10:
    nums = [j for j in range(i, i+4)]
    i+=1
    distinct_primes = [set(), set(), set(), set()]
    for j, num in enumerate(nums):
        primes = primeFactors(num)
        for prime in primes:
            distinct_primes[j].add(prime)
    
    distincts = [set(), set(), set(), set()]
    for i, d_primes_set in enumerate(distinct_primes):
        check_against = distinct_primes
        del check_against[i]
        for j in check_against:
            difference = d_primes_set.difference(j)
            for dist in difference:
                print(dist)
                if dist in distincts[i]:
                    distincts[i] = distincts[i].difference(set({dist}))
                else:
                    distincts[i].add(dist)
    found = True
    for distinct in distincts:
        if len(distinct) == 0:
            found = False
            
    if found:
        print(distincts)
        break
