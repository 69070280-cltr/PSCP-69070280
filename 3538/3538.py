"""[LEARNING LOGS] B - Fully pair?"""
def main():
    """[LEARNING LOGS] B - Fully pair?"""
    n = input()
    result = ""
    for i in n:
        if n.count(i) % 2 == 1 and i not in result:
            result += i
    if len(result) > 0:
        print(result)
    else:
        print("fully paired")
main()
