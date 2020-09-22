# PROBLEM 12 - (09/05)
start_time = time.clock_gettime_ns(0)

def compute_triangle_num(index):
    ret = 0
    for i in range(index):
        ret+=i
    return ret

def get_factors(index):
    ret = []
    upto = index**(1/2)
    for i in range(1, round(upto)+1):
        if index % i == 0:
            ret.append(i)
            if i != int(index/i):
                ret.append(int(index/i))
    return ret

factors = []
i = 1
while len(factors) < 500:
    triangle_num = compute_triangle_num(i)
    factors = get_factors(triangle_num)
    i+=1

print("value: " + str(triangle_num))
print("index: " + str(i-1))
end_time = time.clock_gettime_ns(0)
print("This solution took {} s".format((end_time-start_time)*1e-9))
