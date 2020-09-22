# PROBLEM 21 - (09/09)
    # brute-force
    # optimizing
        # only go through 1-10000 in one for loop
        # if you find the pair, 
import time
start_time = time.clock_gettime_ns(0)

def get_proper_divisors(index):
    ret = set()
    upto = index**(1/2)
    for i in range(1, round(upto)+1):
        if index % i == 0:
            ret.add(i)
            if i != int(index/i) and int(index/i) != index:
                ret.add(int(index/i))
    return ret

def d(num):
    return sum(get_proper_divisors(num))


amicable_numbers = set()
amicable_numbers_pairs = []
for i in range(10000):
    a = d(i)
    b = d(a)
    if i == b and i != a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
            amicable_numbers_pairs.append([a, b])
                
print(sum(amicable_numbers))
end_time = time.clock_gettime_ns(0)
print("This solution took {} s".format((end_time-start_time)*1e-9))
