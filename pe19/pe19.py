# PROBLEM 19 - (09/08)
start_time = time.clock_gettime_ns(0)


days = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 
        'July':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31} # Feb has 29 on leap year
days_leapyear = {'Jan':31, 'Feb':29, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 
        'July':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31} # Feb has 29 on leap year

year = 1901  # Tuesday, Jan 1, 1901
pointer = 6 # Sunday, Jan 6, 1901

counter = 0

for year in range(1901, 2001):
    if year % 4 == 0:
        calendar = days_leapyear
    else:
        calendar = days
        
    for month in calendar:
        while pointer < calendar[month]:
            pointer+=7
        if pointer - calendar[month] == 1:
            counter+=1
        pointer = pointer-calendar[month]
    
        
print(counter)
end_time = time.clock_gettime_ns(0)
print("This solution took {} ms".format((end_time-start_time)*1e-6))

