"""[LEARNING LOGS] CuteCat CuteFox"""
def main():
    """[LEARNING LOGS] CuteCat CuteFox"""
    n = int(input())
    d = {}
    for _ in range(n):
        line = input().strip().strip("{}")
        name, num = line.split(":")
        d[num.strip().strip('"')] = name.strip().strip('"')
    if "Cat01" not in d and "Garfield" not in d.values():
        d["Cat01"] = "Garfield"
    if "Fox01" not in d and "Fubuki" not in d.values():
        d["Fox01"] = "Fubuki"
    cats = []
    foxes = []
    for num, name in d.items():
        if num.startswith("Cat"):
            cats.append((int(num[3:]), name, num))
        else:
            foxes.append((int(num[3:]), name, num))
    cats.sort()
    foxes.sort()

    print("Cat :", len(cats))
    print("Fox :", len(foxes))
    for _, name, num in cats:
        print(name, ":", num)
    for _, name, num in foxes:
        print(name, ":", num)
main()
