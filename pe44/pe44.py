
import time
start_time = time.clock_gettime_ns(0)

def pentagonal():
    c = 5 - 2
    a = b = 1
    while True:
        yield a
        b+=c
        a+=b


def sum_diff_pentagonal():
    seen = set()
    for i in pentagonal():
        for j in seen:
            if i - j in seen and i-2*j in seen:
                yield i-j, j
        seen.add(i)
    
it = sum_diff_pentagonal()
print(next(it))


end_time = time.clock_gettime_ns(0)
print("The solution took {} s".format((end_time-start_time)*1e-9))
