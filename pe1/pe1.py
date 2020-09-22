# PROBLEM 1 - (09/02)

result = 0
for num in range(1000):
    if (num % 3 == 0) or (num % 5 == 0):
        result+=num

print(result)
