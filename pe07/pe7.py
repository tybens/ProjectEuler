# PROBLEM 7 - (09/03)

# brute-force:
def isprime(num):    
    upto = num**(1/2)    
    if num==1:
        return False
    for i in range(2, round(upto)+1):
        if num % i == 0:
            return False
    return True

count = 1 # assuming zero-starting
test = 3
while True:
    test+=2
    if isprime(test):
        count+=1
    if count == 10001:
        break
    
print(test)
