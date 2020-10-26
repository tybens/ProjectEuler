# PROBLEM 2 - (09/02)

result = 0
num1 = 1
num2 = 2

while num2 < 4000000:
    if num2 % 2 == 0:
        result+= num2
    oldnum2 = num2
    num2 = num1 + num2
    num1 = oldnum2

print(result)

