"""[LEARNING LOGS] BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())
big = min(b, goal // 5)
remaining = goal - big * 5
if remaining <= a:
    print(remaining)
else:
    print(-1)
