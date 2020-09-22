# PROBLEM 26 - (09/04)
    # the key is that you can't see the same remainder twice when dividing increments of 10*rem (long division)
    # decimal unless it is repeating.
    # so count numbers until you see one that you've already seen
def recurring_length(d):
    count = 0
    i = 1
    remainders = set()
    while (i*10 % d not in remainders):
        remainders.add(i*10%d)
        i = i*10 % d
        # print("remainders: " + str(remainders))
        count += 1
        if (i*10 % d == 0):
            return 0
    return count


maximum = 0
maxdenom = 0
for denom in range(2, 1000):
    if (recurring_length(denom)>maximum):
        maximum = recurring_length(denom)
        maxdenom = denom

print(maxdenom)
print(maximum)

# learned:
    # how to use python sets
    # long division lol
