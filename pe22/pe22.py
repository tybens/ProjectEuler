# PROBLEM 22 - (09/09)
import pandas as pd
import numpy as np
import string
import time


df = pd.read_csv("https://projecteuler.net/project/resources/p022_names.txt", header=None, keep_default_na=False)
start_time = time.clock_gettime_ns(0)

names_alp = df.T.sort_values(by=0)
names_alp = names_alp.reset_index(drop=True)

d = {ch:n+1 for n, ch in enumerate(string.ascii_lowercase)}
total = 0
for i, name in enumerate(names_alp.values):
    score = 0
    for let in name[0]:
        score+= d[let.lower()]
    score=score*(i+1)
    total+=score
    
print(total)

end_time = time.clock_gettime_ns(0)
print("This solution took {} s".format((end_time-start_time)*1e-9))
