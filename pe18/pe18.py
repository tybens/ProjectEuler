# PROBLEM 18 - (09/08)
    # starting from the bottom, each number above it is given two options of 
    # routes (that have a known max route below it that we have saved. 
    # find that max route for each number on the bottom going up.
    
import pprint
import time
start_time = time.clock_gettime_ns(0)


triangle_string = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 "
        
        
def read_triangle_to_array(long_string):
    array = []
    for i in range(int(len(long_string)/3)):
        array.append(int(long_string[i*3:i*3+2]))
    return array


def triangle_array_to_triangle(triangle_array, length_largest_row):
    grid = []
    zeros = []
    index = 0
    for i in range(length_largest_row-1, -1, -1):
        zeros.append([0]*i)
    for i in range(1, length_largest_row+1):
        row = []
        row.extend(triangle_array[index:index+i])
        row.extend(zeros[i-1])
        index = index+i
        grid.append(row)
    return grid

length_largest_row = 15
triangle_array = read_triangle_to_array(triangle_string)
triangle_grid = triangle_array_to_triangle(triangle_array, length_largest_row)

for i in range(length_largest_row-2, -1, -1):
#     pprint.pprint(triangle_grid) 
#     print("\n")
    for j in range(length_largest_row-2, -1, -1):
        triangle_grid[i][j]+= max(triangle_grid[i+1][j], triangle_grid[i+1][j+1])

end_time = time.clock_gettime_ns(0)
print("This solution took {} ms".format((end_time-start_time)*1e-6))

print(triangle_grid[0][0])
