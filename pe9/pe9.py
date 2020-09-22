# PROBLEM 9 - (09/03)

# brute-force
import math



def pythagTriplet(a, b):
    c = math.isqrt(a**2 + b**2)
    if c == (a**2 + b**2)**(1/2):
        return True
    else:
        return False


def pythagorean_triplet_1000():
    for a in range(1, 334): # max is 332 for a
        for b in range(a, 500): # max is 499 for b
            c = 1000-a-b
            if a**2 + b**2 == c**2:
                print("a: {} b: {} c: {}".format(a, b, c))
                return a*b*c

# optimize
    # can break loop once found (only one solution)
    # Dickson's Formula for pythagoras triplets
    
