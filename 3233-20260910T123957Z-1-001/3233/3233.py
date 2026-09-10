"""[LEARNING LOGS] สลากกินแบ่ง"""
a, b = map(str, input().split())
c, d = map(str, input().split())
luck = 0
if a == c and b == d:
    luck = 1000000
elif b == d and a != c:
    luck = 100000
elif a == c and b[2:5] == d[2:5]:
    luck = 2000
elif a == c and b[3:5] == d[3:5]:
    luck = 1000
elif a != c and b[2:5] == d[2:5]:
    luck = 200
elif a != c and b[3:5] == d[3:5]:
    luck = 100
elif a == c and b != d:
    luck = 20
else:
    luck = 0
print(luck)
