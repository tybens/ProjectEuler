# PROBLEM 34 - (09/13)

def factorial(num):
    res = 1
    for i in range(num, 0, -1):
        res=res*i
    return res

def digitFactorial(num):
    ret = 0
    for i in str(num):
        ret+= factorial(int(i))
    return ret

# visualizing upper limit
low = 1000000
upperlimit = 2100000
X = [i for i in range(low, upperlimit)]
y = [digitFactorial(i) for i in X]
import matplotlib.pyplot as plt
plt.figure(figsize=(16,8))
plt.plot(X, y, linewidth=4);
plt.plot(X, X, linewidth=4);

res = 0
for i in range(10, 2000000):
    if i == digitFactorial(i):
        res+=i
print(res)
