# PROBELM 40 - (09/18)
    # d_1 = 1
    # d_10 = 1
    # d_100 = ...
    
# n = 10:29 evens are 1's, odds are 1-9
# n = 30:49 even = 2, 50:69 even = 3, 70:89 even = 4, 90:109 even 5, 110
# 190 every 3rd is 1, every 3rd+1 is 2, every 3rd plus 2 is 1-9, 
one_to_nine = 9

n = 1
digit = 1
remember = set((1, 10, 100, 1000, 10000, 100000, 1000000))
rem = set()
found = False
while n <= 1000000:
    if n in remember:
        rem.add((n, digit))

    #check for n = 10,000
    if n >= 10000 and not found:
        found = True
        rem.add((n, digit))

    if digit < 10:
        n+=1
    elif digit < 100:
        n+=2
    elif digit < 1000:
        n+=3
    elif digit < 10000:
        n+=4
    elif digit < 100000:
        n+=5
    elif digit < 1000000:
        n+=6
    digit+=1
    
print(rem) 
# 10,000 doesn't match up perfectly with the start of an integer
# but 9,998 matches with 2777, so 10,000 is 7
print("expression yields: " + str(1*1*5*3*7*2*1))


