"""Primary Color"""
x = input()
y = input()
if x + y == "RedBlue" or x + y == "BlueRed":
    print("Violet")
elif x + y == "RedYellow" or x + y == "YellowRed":
    print("Orange")
elif x + y == "BlueYellow" or x + y == "YellowBlue":
    print("Green")
elif x + y == "RedRed":
    print("Red")
elif x + y == "BlueBlue":
    print("Blue")
elif x + y == "YellowYellow":
    print("Yellow")
else:
    print("Error")
