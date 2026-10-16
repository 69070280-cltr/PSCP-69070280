"""[LEARNING LOGS] Duplicate I"""
def main():
    """[LEARNING LOGS] Duplicate I"""
    m = int(input())
    n = int(input())
    l1 = []
    l2 = []
    l3 = []
    for _ in range(m):
        m_id = input()
        l1.append(m_id)
    for _ in range(n):
        n_id = input()
        l2.append(n_id)
    for i in l1:
        if i in l2:
            l3.append(i)
    if l3:
        print("\n".join(sorted(l3, reverse=True)))
    else:
        print("Nope")
main()
