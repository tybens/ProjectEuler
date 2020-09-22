# PROBLEM 31 - (09/12) 
    # second try
    # dynamic programming

coins = [2, 5, 10, 20, 50, 100, 200]
ways = [1 for i in range(201)] # initalize to 1 because all 1's catch case


for coin in coins:
    for i in range(201):
        if i >= coin:
            ways[i]+=ways[i-coin]


ways
