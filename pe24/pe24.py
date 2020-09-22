# PROBLEM 24 - (09/09)
    #
    
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

length = len(digits)
count = 0

# while count <= 1e6:
#     i = length - 1
#     while i > 0:
#         if digits[i] > digits[i-1]:
#             temp = digits[i-1]
#             digits[i-1] = digits[i]
#             digits[i] = temp
#             break
#         elif digits[i] < digits[i-1]:
#             temp = digits[i-1]
#             digits[i-1] = digits[i]
#             digits[i] = temp
#             i-=1
#     print(digits)
            

for _ in range(1, 1000000):      # including the first [0, 1, 2, 3,...] as a perm     

    i = len(digits) - 1

    # find i such that digits[i:] is the largest sequence with 
    # elements in descending lexicographic order 
    while i > 0 and digits[i-1] > digits[i]:        
        i -= 1

    # reverse digits[i:] 
    digits[i:] = reversed(digits[i:])  


    if i > 0: 

        q = i 
        # find q such that digits[q] is the smallest element 
        # in digits[p:] such that digits[q] > digits[i - 1] 
        while digits[i-1] > digits[q]:   
            q += 1

        # swap digits[i - 1] and digits[q] 
        temp = digits[i-1]  
        digits[i-1]= digits[q] 
        digits[q]= temp 

print(digits)
