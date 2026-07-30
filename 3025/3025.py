"""Season"""
def main():
    """Season change"""
    month = int(input())
    day = int(input())
    if month == 3:
        print("spring" if day >= 21 else "winter")
    elif month == 6:
        print("summer" if day >= 21 else "spring")
    elif month == 9:
        print("fall" if day >= 21 else "summer")
    elif month == 12:
        print("winter" if day >= 21 else "fall")
    elif month in [1, 2]:
        print("winter")
    elif month in [4, 5]:
        print("spring")
    elif month in [7, 8]:
        print("summer")
    else:
        print("fall")
main()
