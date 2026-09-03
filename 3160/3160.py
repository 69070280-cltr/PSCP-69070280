"""[LEARNING LOGS] หาจำนวนเฉพาะ"""
n, t = map(int,input().split())
primes = []
for i in range(n,t+1):
    if i < 2:
        continue
    is_prime = True
    for n in range(2,i):
        if not i % n:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
if primes:
    print(*primes)
    print(f"Total primes: {len(primes)}")
else:
    print(f"Total primes: {len(primes)}")
