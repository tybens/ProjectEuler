# PROBELM 33 - (09/13)
    # brute-force
    
import time
start_time = time.clock_gettime_ns(0)

def checkDigitCancel(numer, denom):
    for i, num in enumerate(str(numer)):
        for j, den in enumerate(str(denom)):
            if num == den:
                if int(num) == 0:
                    return False
                if int(str(denom)[1-j]) != 0:
                    check = (numer/denom == int(str(numer)[1-i])/int(str(denom)[1-j]))
                    return check
                else:
                    return False
    
res = []
for denom in range(10, 100):
    for numer in range(10, denom):
        if checkDigitCancel(numer, denom):
            res.append([numer, denom])
        

ans = 1
for i in res:
    ans *= i[0]/i[1]

from fractions import Fraction

print(str(Fraction(ans).limit_denominator())[2:])

end_time = time.clock_gettime_ns(0)
print("The solution took {} ms".format((end_time-start_time)*1e-6))

