"""[LEARNING LOGS] Pad Thai"""
def main():
    """[LEARNING LOGS] Pad Thai"""
    like = {"Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp",
            "Bean Sprouts","Noodle","Chives","Lime","Egg","Oil","Peanuts"}
    taste = {"Sweet","Sour","Salty"}
    set_In = set()
    set_taste = set()
    while True:
        In = input()
        if In == "Cook":
            break
        set_In.add(In)
    while True:
        t = input()
        if t == "End":
            break
        set_taste.add(t)
    if not set_In.issubset(like):
        print("This is not Pad Thai!!!")
    elif set_In != like:
        print("This is bad!")
    elif set_taste != taste:
        print("Not Bad...")
    else:
        print("Delicious!")
main()
