# PROBLEM 29 - (09/09)
    # learned: adding the if statement before adding 
    # a duplicate (that would disappear in the set)
    # makes the solution slower

import time
start_time = time.clock_gettime_ns(0)

distinct_terms = set()
for a in range(2, 101):
    for b in range(2, 101):
        term = a**b
        distinct_terms.add(term)
        
print(len(distinct_terms))

end_time = time.clock_gettime_ns(0)
print("The adding duplicated solution took {} ms".format((end_time-start_time)*1e-6))

        
# if statement solution
        
start_time = time.clock_gettime_ns(0)

distinct_terms = set()
for a in range(2, 101):
    for b in range(2, 101):
        term = a**b
        if term not in distinct_terms:
            distinct_terms.add(term)
        
print(len(distinct_terms))

end_time = time.clock_gettime_ns(0)
print("The if statement solution took {} ms".format((end_time-start_time)*1e-6))
