# 게임 개발
if __name__ == "__main__":

    n, m = map(int, input().split())
    x, y, dir = map(int, input().split())
    dir = 4 - dir
    map = [[i for i in map(int, input().split())] for _ in range(n)]

    count = 1  # 처음 위치 방문 처리
    map[x][y] = 1  # map에서 처음 위치 방문 처리

    # 왼쪽으로 돈다 = index를 +1한다.
    step = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    while True:
        flag = True
        for _ in range(4):
            dir = (dir + 1) % 4  # 왼쪽으로 돌림
            nx = x + step[dir][0]  # nx = 움직인 임시 위치
            ny = y + step[dir][1]  # 왼쪽으로 전진함(앞으로 한 칸 간 셈)

            # 방문한 적 없는 육지일 때
            if map[nx][ny] == 0:
                x, y = nx, ny  # 왼쪽으로 전진함(앞으로 한 칸 간 셈)
                map[nx][ny] = 1  # 가본 육지이므로 1로 바꿈.
                count += 1
                flag = False
                break

            else:  # 왼쪽이 방문한 칸or바다일 때
                nx, ny = x, y
                continue

        if flag == False:
            continue

        # 4칸 다 방문한 칸일 때 -> 바라보는 방향 유지한채 뒤로 한칸 감.
        x = x + step[(dir + 2) % 4][0]
        y = y + step[(dir + 2) % 4][1]

        if map[x][y] == 1:
            break

    print(count)
