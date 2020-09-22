# PROBLEM 42 - (09/18)

import pandas as pd
df = pd.read_csv("https://projecteuler.net/project/resources/p042_words.txt", header=None, keep_default_na=False)


t_n = 1/2 * n * (n + 1)
# the word ZZZZZZZZZ is 
triangle_nums = set()
for i in range(1, 99):
    triangle_nums.add(1/2 * i * (i+1))

values = [i for i in range(1, 26 + 1)]
keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alph_to_num = dict(zip(keys, values))
def wordValue(word):
    value = 0
    if word == True:
        word = str(word).upper()
    for i in word:
        value+=alph_to_num[i]
    return value

count = 0
for i in df.values[0]:
    if wordValue(i) in triangle_nums:
        count+=1

print(count)
