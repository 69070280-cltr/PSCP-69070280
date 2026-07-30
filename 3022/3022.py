"""Temperature"""
x = float(input())
y = input().strip()
z = input().strip()
c = 0.0
result = 0.0
# แปลงเป็น C
if y == "C":
    c = x
elif y == "F":
    c = (x - 32) * 5 / 9
elif y == "K":
    c = x - 273.15
elif y == "R":
    c = (x - 491.67) * 5 / 9
# แปลงจาก C เป็น F K R
if z == "C":
    result = c
elif z == "F":
    result = c * 9 / 5 + 32
elif z == "K":
    result = c + 273.15
elif z == "R":
    result = (c + 273.15) * 9 / 5
print(f"{result:.2f}")
