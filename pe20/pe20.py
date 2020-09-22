# PROBLEM 20 - (09/08)
def factorial(num):
    res = 1
    for i in range(num, 0, -1):
        res=res*i
    return res

the_num = factorial(100)
res = 0

for i in str(the_num):
    res+=int(i)
    
print(res)

