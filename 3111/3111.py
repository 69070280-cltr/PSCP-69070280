"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
import math
M = input()
n = int(input())
total = 0
cost = 0
final = 0
for i in range(1, n+1):
    p = float(input())
    cost += p
    i += 0
    if M == "Y":
        total = cost - (cost * 0.05)
    elif M == "N" and cost >= 500:
        total = cost - (cost * 0.03)
    else:
        total = cost
final = math.ceil(total*100)/100
print(f"{final:.2f}")
