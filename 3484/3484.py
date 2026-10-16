"""[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""
def main():
    """[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""
    n, p = input().split()
    n = int(n)
    p = float(p)
    d = []
    for _ in range(n):
        row = list(map(int,input().split()))
        d.append(row)
    col_tiles = [0]*n
    col_points =[0]*n
    total_tiles = 0
    total_points = 0
    for i in range(n):
        row_tiles = 0
        row_points = 0
        for j in range(n):
            x = d[i][j]
            if x > 0:
                row_tiles += 1
                col_tiles[j] += 1
            row_points += x
            col_points[j] += x
        print(*d[i], row_tiles, row_points)
        total_tiles += row_tiles
        total_points += row_points
    print(*col_tiles)
    print(*col_points)
    print(total_tiles, total_points, f"{total_points * p:.2f}")
main()
