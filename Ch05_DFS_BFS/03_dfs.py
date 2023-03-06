# 3번 문제를 DFS로 풀음
import sys

sys.stdin = open("Ch05_DFS_BFS/ice_maker.txt", "r")
n, m = map(int, input().split(" "))

mold = []
for _ in range(n):
    mold.append([int(i) for i in list(input())])

# dfs 방식으로 한번에 만들 수 있는 얼음 수 return하기.
# n x m 크기의 리스트 (0~n-1행, 0~m-1열)
visit = []
search = [(0, -1), (0, 1), (1, 0), (-1, 0)]
count = 0

for mold_list in mold:  # 1(칸막이)는 True로 지정하여 방문하지 않게 함.
    visit.append([True if num == 1 else False for num in mold_list])

# DFS 구현 위해 재귀함수 사용
def dfs(row, col):
    visit[row][col] = True
    row_, col_ = row, col

    for dir in search:  # 상,하,좌,우에
        r, c = row_ + dir[0], col_ + dir[1]
        # 범위 안의 index이고, 방문한 적 없는 구멍이면 dfs() 재귀적으로 호출함.
        if 0 <= r < n and 0 <= c < m and visit[r][c] == False:
            dfs(r, c)


for row in range(n):
    for col in range(m):
        # 칸막이가 있는 칸이거나 이미 방문한 칸(구멍)일 때.
        if visit[row][col] == True:
            continue
        # 방문하지 않은 구덩이인 경우
        count += 1
        dfs(row, col)


print(count)
