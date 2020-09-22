# PROBLEM 32 - (09/12)
    # brute-force,
    # need to look into space trimming and optimization

from itertools import permutations   
import time
start_time = time.clock_gettime_ns(0)

def convert(lists): 
      
    # Converting integer list to string list 
    # and joining the list using join() 
    res = int("".join(map(str, lists))) 
      
    return res 
  

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
perm = list(permutations(nums))
save = []
for test in perm:
    nums = test
    
    for i in range(1, 4):
        mult = nums[:i]

        for j in range(i+1, 6):
            mcand = nums[i:j]
            prod = nums[j:]
            testing = list(map(convert, [mult, mcand, prod]))
            if testing[0]*testing[1]== testing[2]:
                save.append((testing[0], testing[1], testing[2]))
    
total_sum = sum(set([i[2] for i in save]))
print(total_sum)

end_time = time.clock_gettime_ns(0)
print("The solution took {} s".format((end_time-start_time)*1e-9))
