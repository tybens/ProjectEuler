# PROBLEM 45 - (09/19)
    # all hexagonal numbers are triangular numbers
        # so can get rid of triangular numbers and find the second time that hexagonal
        # matches pentagonal

import time
start_time = time.clock_gettime_ns(0)

def polygonal(s):
    c = s - 2
    a = b = 1
    while True:
        yield a
        b+=c
        a+=b
        

P_it = polygonal(5)
H_it = polygonal(6)
P_seen = set()
H_seen = set()

found_first_one = False # first one is 40755, we want the second one.
while True:
    this = next(P_it)
    P_seen.add(this)
    if this in H_seen:
        if found_first_one:
            print(this)
            break
        found_first_one = True
    H_seen.add(next(H_it))
    

end_time = time.clock_gettime_ns(0)
print("The solution took {} ms".format((end_time-start_time)*1e-6))
