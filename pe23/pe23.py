# PROBLEM 23 - (09/09)
    # brute-force
    # learned more about itertools and sets() [specifically combinations_with_replacement]
    # 
import itertools
import time
start_time = time.clock_gettime_ns(0)


def get_proper_divisors(num):
    upto = num**(1/2)
    res = set()
    for i in range(1, round(upto)+1):
        if num % i == 0:
            if num/i != num:
                res.add(num/i)
            res.add(i)
    return res

def is_abundant(num):
    ret = sum(get_proper_divisors(num)) > num
    return ret

abundant_numbers = set()
upper_limit = 28123
for i in range(1, upper_limit+1):
    if is_abundant(i):
        abundant_numbers.add(i)
        
can_be_expressed = set()
for nums in itertools.combinations_with_replacement(list(abundant_numbers), 2):
    can_be_expressed.add(sum(nums))
            
total = 0
for i in range(1, upper_limit+1):
    if i not in can_be_expressed:
        total+=i
print(total)



end_time = time.clock_gettime_ns(0)
print("This solution took {} s".format((end_time-start_time)*1e-9))
