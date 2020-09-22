# PROBLEM 28 - (09/09)
    # learned: don't always need to find a formula
    # (although it may be interesting to come back and derive it)
    
total = 0
pointer = 1
i = 1
while i < 501:
    for _ in range(4):
        total+= pointer
        pointer+= 2*i # add evens
    i+=1 # every 4 times
    
total+=pointer # one last time to round out the spiral

print(total)
