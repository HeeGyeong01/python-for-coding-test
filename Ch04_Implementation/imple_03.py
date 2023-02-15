# 왕실의 나이트
if __name__ == "__main__":

    """내가 짠 코드
    col = ["a", "b", "c", "d", "e", "f", "g", "h"]

    location = input()  # ex) a1 들어옴
    loc_col = col.index(location[0]) + 1  # a
    loc_row = int(location[1])  # 1

    d_row = [-2, -2, 2, 2, -1, -1, 1, 1]
    d_col = [-1, 1, -1, 1, -2, 2, -2, 2]

    count = 0
    for i in range(8):
        if 0 < (loc_row + d_row[i]) < 9 and 0 < (loc_col + d_col[i]) < 9:
            count += 1

    print(count)
    """

    # 책에 나온 정답코드
    loc = input()  # ex) a1 들어옴
    loc_col = ord(loc[0]) - ord("a") + 1  # a
    loc_row = int(loc[1])  # 1

    count = 0
    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    for step in steps:
        row = loc_row + step[0]
        col = loc_col + step[1]

        if (0 < row < 9) and (0 < col < 9):
            count += 1

    print(count)
