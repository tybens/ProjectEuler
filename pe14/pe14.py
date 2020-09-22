# PROBLEM 14 - (09/05)
    # optimize by saving past numbers in a dictionary
start_time = time.clock_gettime_ns(0)

max_count = 0
for start_num in range(1, 1000000):
    num = start_num
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = 3*num + 1
        count+=1
    if count > max_count:
        max_start_num = start_num
        max_count = count

print("Starting Number: {}\nMaximum Count: {}".format(max_start_num, max_count))

end_time = time.clock_gettime_ns(0)
print("This solution took {} s".format((end_time-start_time)*1e-9))

