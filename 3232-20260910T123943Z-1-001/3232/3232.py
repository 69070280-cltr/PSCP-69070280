"""[LEARNING LOGS] กบน้อยกระโดด"""
x, y = map(int,input().split())
count = 0
total = 0
current = x
while total < y:
    if current < 1:
        count = -1
        break
    total += current
    count += 1
    current -= 2
print(count)
