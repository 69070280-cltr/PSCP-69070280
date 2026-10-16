"""[LEARNING LOGS] Giraffe"""
def main():
    """[LEARNING LOGS] Giraffe"""
    n = int(input())
    num = [int(input()) for _ in range(n)]
    count = 0
    if n == 1:
        print(1)
        return
    if num[0] > num[1]:
        count += 1
    if num[-1] > num[-2]:
        count += 1
    for i in range(1, n-1):
        if num[i] > num[i-1] and num[i] > num[i+1]:
            count += 1
    print(count)
main()
