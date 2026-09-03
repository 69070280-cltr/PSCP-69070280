"""[LEARNING LOGS] ของขวัญและขโมย"""
n, k, t = map(int,input().split())
current = 1
count = 1
if t == 1:
    print(1)
else:
    while True:
        current = ((current - 1 + k) % n) + 1
        if current == t:
            count += 1
            break
        if current == 1:
            break
        count += 1
    print(count)
