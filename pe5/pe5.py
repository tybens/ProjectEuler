# PROBLEM 5 - (09/03)
    # if divisible by 20 it is also divisible by 10 and 2
    # 19
    # if diviisble by 18 it is also divisible by 9 and 2 and 6 and 3
    # 17
    # 16 -> 4 and 4 and 8 and 2
    # 15 -> 5 and 3
    # 14 -> 7 and 2
    # 13
    # 12 -> 6
    # 11

    
division = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
result = 0
loop = True

while(loop):
    result+=20
    
    loop = False
    for i in division:
        if result % i != 0:
            loop = True
            

print(result)

