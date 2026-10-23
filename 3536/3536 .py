"""[LEARNING LOGS] isPrime_large"""
def main():
    """[LEARNING LOGS] isPrime_large"""
    n = int(input())
    count = True
    if n < 2:
        count = False
    i = 2
    while i * i <= n:
        if not n % i:
            count = False
            break
        i += 1
    if count:
        print("YES")
    else:
        print("NO")
main()
