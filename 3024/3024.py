"""Surprising Check"""
def main():
    """Check if surprising score combination exists."""
    total = float(input())
    highest = float(input())
    surprising = False
    # วนลูปตรวจสอบคะแนนที่เป็นไปได้
    for a_int in range(101):
        for b_int in range(101):
            a = a_int / 10.0
            b = b_int / 10.0
            c = total - a - b
            if 0 <= c <= 10:
                scores = (a, b, c)
                if max(scores) == highest and max(scores) - min(scores) > 2:
                    surprising = True
                    break
        if surprising:
            break
    if surprising:
        print("Surprising")
    else:
        print("Not surprising")
main()
