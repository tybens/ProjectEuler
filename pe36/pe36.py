# PROBLEM 36 - (09/14)

import math

def check_palindrome_of_number(number):
    a = str(number)
    for i in range(math.floor(len(a)/2)):
        if a[i] != a[len(a)-i-1]:
            return False
    return True


numbers = []
for i in range(1000000):
    if check_palindrome_of_number(i) and check_palindrome_of_number(format(i, 'b')):
        numbers.append(i)
print(numbers)
print(sum(numbers))
