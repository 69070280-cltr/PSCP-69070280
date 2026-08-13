"""[LEARNING LOGS] A-E-I-O-U"""
n = input()
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for ch in n:
    if ch in "a,A":
        count_a += 1
    elif ch in "e,E":
        count_e += 1
    elif ch in "i,I":
        count_i += 1
    elif ch in "o,O":
        count_o += 1
    elif ch in "u,U":
        count_u += 1
if count_a >0:
    print("a :", count_a)
if count_e >0:
    print("e :", count_e)
if count_i >0:
    print("i :", count_i)
if count_o >0:
    print("o :", count_o)
if count_u >0:
    print("u :", count_u)
