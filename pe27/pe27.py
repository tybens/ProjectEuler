# PROBLEM 27 - (09/09)
    # some (probably trivial) optimizations
        # b has to be prime (and thus positive!...)
        # 1 + a + b has to be prime
        # n(n + a) + b has to be prime
import time
start_time = time.clock_gettime_ns(0)
        
def isprime(num):
    upto = num**(1/2)    
    if num<=1:
        return False
    for i in range(2, round(upto)+1):
        if num % i == 0:
            return False
    return True


def quadratic_primes(a, b):
    n = 0
    while True:
        num = n**2 + a*n + b
        if not isprime(num):
            return n
        n+=1
        
Bs = []
for b in range(1, 1001):
    if isprime(b):
        Bs.append(b)

As = [i for i in range(-1000, 1000)]


maxnum = 0
for b in Bs:
    for a in As:
        thisnum = quadratic_primes(a, b)
        if thisnum > maxnum:
            maxnum = thisnum
            coeffs = [a, b]


product = coeffs[0]*coeffs[1]
print("prod of coeffs is: {}".format(product))
print("max number n is: {}".format(maxnum))
print("coeffs are: {}".format(coeffs))

end_time = time.clock_gettime_ns(0)
print("This solution took {} s".format((end_time-start_time)*1e-9))
