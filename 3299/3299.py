"""[LEARNING LOGS] แปลงดอกไม้"""
def main():
    """[LEARNING LOGS] แปลงดอกไม้"""
    l, n = map(int,input().split())
    d = 0
    while d * (d+1)//2 < n:
        d += 1
    b = (d+l-1)//l
    print(b)
main()
