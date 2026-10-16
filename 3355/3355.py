"""[LEARNING LOGS] Shorten"""
def main():
    """[LEARNING LOGS] Shorten"""
    m = []
    while True:
        n = int(input())
        if n == -1:
            break
        m.append(n)
    p = []
    s = 0
    for i, val in enumerate(m):
        if i == len(m)-1 or m[i+1] != m[i] + 1:
            if m[s] == val:
                p.append(str(val))
            else:
                p.append(f"{m[s]}-{val}")
            s = i+1
    print(", ".join(p))
main()
