"""[LEARNING LOGS] ส่งต่อ"""
def main():
    """[LEARNING LOGS] ส่งต่อ"""
    n, s = map(int,input().split())
    l = [0]
    for _ in range(n):
        tell = int(input())
        l.append(tell)
    got = set()
    c = s
    while c and c not in got:
        got.add(c)
        c = l[c]
    print(len(got))
main()
