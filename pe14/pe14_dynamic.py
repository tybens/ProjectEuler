# dynamic programming - 
    # staring at and trying to understand dabslee's code
    # and then remaking it from memory / understanding
    # learned about floor division
    # 
chainlengths = [0, 1]
def length_chain(num):
    if num > len(chainlengths):
        if num % 2 == 0:
            return length_chain(num//2) + 1
        else:
            return length_chain(num*3+1) + 1
    if chainlengths[num] != 0:
        return chainlengths[num]
    if num % 2 == 0:
        chainlengths[num] = length_chain(num//2) + 1
        return chainlengths[num]
    else:
        chainlengths[num] = length_chain(num*3+1) + 1
        return chainlengths[num]

chainlengths.extend([0]*1000000)

maxlen = 0
for i in range(1, 1000000):
    mylen = length_chain(i)
    if mylen > maxlen:
        maxlen = mylen
        maxindex = i
print(maxindex)
