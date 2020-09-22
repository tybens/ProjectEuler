# PROBELM 50 (09/21)
    # Consecutive prime sum
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

upto = 1000000
primes = sieveEratosthenes(upto)
lengthPrimes = 0
primeSum = []
total = 0
for prime in primes:
    total+=prime
    primeSum.append(total)

for i in range(len(primes)):
    for j in range(i-lengthPrimes+1, -1, -1):
        summed = primeSum[i] - primeSum[j]
        if summed > upto:
            break
        if summed in primes:
            lengthPrimes = i - j
            ret = summed

            
print(ret)
print("consisting of {} primes".format(lengthPrimes))
print("THESE: {}".format(primes[remj:remi]))
