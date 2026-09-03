"""[LEARNING LOGS]เกมสะสมแต้ม"""
n = int(input())
total = 0
for i in range(n):
    tp = input()
    i += 0
    if tp == "+":
        total += 10
    elif tp == "-":
        total -= 5
print(total)
