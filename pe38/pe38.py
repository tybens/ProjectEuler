# PROBLEM 38 - (09/17)
    # brute-force

import time
start_time = time.clock_gettime_ns(0)

def isPandigital(str_num):
    nums = set()
    for i in str_num:
        if i in nums or i == '0':
            return False
        nums.add(i)
    return True


pandigitals = []
n = 1
myMax = 0
while n < 50000:
    i = 0
    pandigital = ''
    while len(pandigital) < 9:
        i+=1
        pandigital+=str(n*i)
        
    if isPandigital(pandigital):
        if int(pandigital) > myMax:
            myMax = int(pandigital)
        pandigitals.append((pandigital, n, i))
    n+=1

print(pandigitals[-1])
print(myMax)


end_time = time.clock_gettime_ns(0)
print("The solution took {} s".format((end_time-start_time)*1e-9))
