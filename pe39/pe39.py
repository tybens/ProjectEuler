# PROBLEM 39 - (09/17)
    # brute-force disgusting


def pythagorean_triplet_variable_p(perim):
    count = 0
    for a in range(1, perim): # max is 332 for a
        for b in range(a, perim): # max is 499 for b
            c = perim-a-b
            if a**2 + b**2 == c**2:
                count+=1
    return count
            
maxAmount = 0
maxP = 0
for p in range(1, 1001):
    thisAmount = pythagorean_triplet_variable_p(p)
    if maxAmount < thisAmount:
        maxAmount = thisAmount
        maxP = p

        

