# PROBLEM 49 (09/22)

def sieveEratosthenes(upto):
    i = 2
    ret = [0, 0]
    ret.extend([j for j in range(2, upto+1)])
    while i <= upto:
        it = ret[i]
        if it != 0:
            increment = it
            it+=increment
            while it <= upto:
                ret[it] = 0
                it+=increment
        i+=1
    primes = []
    for prime in ret:
        if prime != 0:
            primes.append(prime)
            
    return primes
    
def isNumberPermutation(num1, num2, num3):
    num1_set = set()
    num2_set = set()
    num3_set = set()

    for i, n in enumerate(str(num1)):
        num1_set.add(int(n))
        num2_set.add(int(str(num2)[i]))
        num3_set.add(int(str(num3)[i]))

    if num1_set == num2_set and num1_set == num3_set:
        return True
    return False
        
primes = sieveEratosthenes(10000)
check = []
for prime in primes:
    if prime > 999:
        check.append(prime)
        
for prime in check:
    terms = [prime, prime+3330, prime+3330*2]
    if terms[1] in check:
        if terms[2] in check:
            if isNumberPermutation(terms[0], terms[1], terms[2]):
                print("{}, {}, {}".format(prime, prime+3330, prime+3330*2))

