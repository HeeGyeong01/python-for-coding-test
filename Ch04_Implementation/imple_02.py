if __name__ == "__main__":

    # 내가 짠 코드
    h = int(input())
    m = 59
    s = 59

    mxs = (15 * 45) * 2 + (15 * 15)

    if 3 <= h:
        print(h * mxs + 3600)
    else:
        print((h + 1) * mxs)

    """ 책의 정답 코드
    h = int(input())
    count = 0

    for h in range(h + 1):
        for m in range(60):
            for s in range(60):
                time = str(h) + str(m) + str(s)

                if "3" in time:
                    count += 1

    print(count)
    """
