"""[LEARNING LOGS] หั่นขนมปัง"""
def main():
    """[LEARNING LOGS] หั่นขนมปัง"""
    w, h, m, n = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    xs = [0] + xs + [w]
    ys = [0] + ys + [h]
    l1 = []
    l2 = []
    for i in range(m + 1):
        l1.append(xs[i + 1] - xs[i])
    for b in range(n + 1):
        l2.append(ys[b + 1] - ys[b])
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    f = l1[0] * l2[0]
    s = max(l1[0] * l2[1], l1[1] * l2[0])
    print(f, s)
main()
