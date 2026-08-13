"""[LEARNING LOGS] ปราสาท"""
n = int(input())
row = 1
while row ** 2 < n:
    row += 1
position = n - (row - 1) ** 2
if position % 2 == 1:
    print(2 * (row - 1))
else:
    print(2 * (row - 1) - 1)
