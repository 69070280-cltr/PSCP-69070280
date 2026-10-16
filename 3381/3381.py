"""[LEARNING LOGS] Point Sorting"""
def main():
    """[LEARNING LOGS] Point Sorting"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = []
        for _ in range(n):
            x, y = map(int,input().split())
            l.append((x+y, -y , x, y))
        l.sort()
        for _, _, x, y in l:
            print(x, y)
main()
