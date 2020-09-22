# PROBLEM 25 - (09/09)
    # learned: int is of unlimited size. but 1e1000 produces inf... don't really know why
    
def fibonacci(term):
    a = 1 # 1st term
    b = 1 # 2nd term
    for i in range(3, term+1):
        temp = b
        b += a
        a = temp
    return b

def num_digits(num):
    return len(str(num))

i = 1
while True:
    what = num_digits(fibonacci(i))
    if what==1000:
        long_num = fibonacci(i)
        index = i
        break
    i+=1

print(index) 
