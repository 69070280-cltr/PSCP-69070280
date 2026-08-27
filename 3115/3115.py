"""[LEARNING LOGS] Arcade of Time: Store Check"""
num, check = map(int, input().split())
store = []
for i in range(num):
    s, e = map(int,input().split())
    i += 0
    store.append((s,e))
time = list(map(int,input().split()))
result = []
for n in time:
    count = 0
    check += 0
    for s, e in store:
        if s <= n < e:
            count += 1
    result.append(count)
print(*result)
