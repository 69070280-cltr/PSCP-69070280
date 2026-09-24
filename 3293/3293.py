"""[LEARNING LOGS] BigFrame"""
def main():
    """[LEARNING LOGS] BigFrame"""
    t1 = input().rstrip()
    t2 = input().rstrip()
    t3 = input().rstrip()
    t4 = input().rstrip()
    t5 = input().rstrip()
    w = max(len(t1), len(t2), len(t3), len(t4), len(t5))
    print("*"*(w+4))
    print("*" + " " + t1 + " "*(w-len(t1)+1) + "*")
    print("*" + " " + t2 + " "*(w-len(t2)+1) + "*")
    print("*" + " " + t3 + " "*(w-len(t3)+1) + "*")
    print("*" + " " + t4 + " "*(w-len(t4)+1) + "*")
    print("*" + " " + t5 + " "*(w-len(t5)+1) + "*")
    print("*"*(w+4))
main()
