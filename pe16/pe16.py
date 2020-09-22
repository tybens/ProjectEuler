# PROBLEM 16 - (09/08)
    # pretty trivial in python

num = 2**1000
str_num = str(num)
res = 0
for i in range(len(str_num)):
    res+=int(str_num[i])
            
print(res)
    
