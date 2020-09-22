# PROBLEM 30 - (09/11)


def sum_of_digits_five_pow(num):
    res = 0
    for i in str(num):
        res+= int(i)**5
    return res

# establishing upper limit
import matplotlib.pyplot as plt

X = [i for i in range(1, 300001)]
y = [sum_of_digits_five_pow(i) for i in X]

plt.figure(figsize=(16,8))
plt.plot(X, y, linewidth=4);
plt.plot(X, X, linewidth=4);


# brute-force
nums = []
for i in range(1, 240000):
    if i == sum_of_digits_five_pow(i):
        nums.append(i)
        
print(sum(nums))
