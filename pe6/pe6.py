# PROBLEM 6 - (09/03)

def sum_of_squares(top_num):
    ret = 0
    for num in range(1, top_num+1):
        ret+=num**2
    return ret

def sq_of_sum(top_num):
    ret = 0
    for num in range(1, top_num+1):
        ret+=num
    return ret**2

N = 100
print(sq_of_sum(N)-sum_of_squares(N))

# optimized if I find converged geometric series and subtract the difference
