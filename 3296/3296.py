"""[LEARNING LOGS] RGB Mixed"""
def main():
    """[LEARNING LOGS] RGB Mixed"""
    r1, g1, b1 = map(int,input().split())
    r2, g2, b2 = map(int,input().split())
    mix_r = (r1 + r2) // 2
    mix_g = (g1 + g2) // 2
    mix_b = (b1 + b2) // 2
    print(mix_r,mix_g,mix_b)
main()
