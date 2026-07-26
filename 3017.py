"""Bills"""
x = int(input())
service = x * 0.1
if service < 50:
    service = 50
elif service > 1000:
    service = 1000
total = x + service
vat = total * 0.07
total_price = total + vat
print(f"{total_price:.2f}")
