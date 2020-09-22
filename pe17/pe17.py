# PROBLEM 17 - (09/08)

one_to_nine = 36
ten_to_nineteen = 70
tens = (6+6+5+5+5+7+6+6)    # twenty, thirty... ninety
one_to_ninetynine = tens*10+one_to_nine*9+ten_to_nineteen

hundred = 7
_and = 3
                    # 100, 200   # 101, 102                                 # one <- hundred and 
onehundred_to_999 = 9*hundred + (99*9*(hundred+_and)) + 10*one_to_ninetynine + 100*one_to_nine

onehundred_to_1000 = onehundred_to_999 + 11  # for { onethousand = 11 }

print(onehundred_to_1000)
