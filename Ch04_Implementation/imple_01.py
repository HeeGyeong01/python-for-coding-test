if __name__ == "__main__":

    n = int(input())
    arr = input().split()

    print(arr)
    print(type(arr))

    row = 1
    col = 1

    for dir in arr:

        if dir == "L":
            col = (col - 1) if (col + 1) > 0 else col

        elif dir == "R":
            col = (col + 1) if (col + 1) > 0 else col

        elif dir == "U":
            row = (row - 1) if (row - 1) > 0 else row

        elif dir == "D":
            row = (row + 1) if (row + 1) > 0 else row

    print(row, col)
