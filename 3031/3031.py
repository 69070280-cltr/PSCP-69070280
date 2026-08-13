"""[LEARNING LOGS] Ink"""
import math
S, N = map(int, input().split())
answer = []
for i in range(N):
    x, y = map(int, input().split())
    area = 3.1416 * (x**2 + y**2)
    i += 0
    time = math.ceil(area / S)
    answer.append(time)
for t in answer:
    print(t)
