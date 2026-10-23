"""[LEARNING LOGS] Impostor"""
def main():
    """[LEARNING LOGS] Impostor"""
    player = {}
    out = {}
    while True:
        n = input()
        if n == "Start":
            break
        n = n.strip('{}').replace('"','')
        name, role = n.split(":")
        player[name.strip()] = role.strip()
    while True:
        s = input()
        if s == "End":
            break
        out[s] = player.pop(s)
    count = list(player.values()).count("Impostor")
    print(count, "Impostor Remains")
    print("***Alive***")
    for i in sorted(player):
        print(i, ":", player[i])
    print("***Dead***")
    for dead in sorted(out):
        print(dead, ":", out[dead])
main()
