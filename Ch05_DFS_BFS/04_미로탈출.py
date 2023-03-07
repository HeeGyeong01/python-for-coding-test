# 미로탈출-bfs
import sys
from collections import deque

sys.stdin = open("Ch05_DFS_BFS/maze_1.txt", "r")
n, m = map(int, input().split(" "))

graph = [list(map(int, list(input()))) for _ in range(n)]
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs(row, col):
    que = deque()
    que.append((row, col))

    while que:
        row, col = que.popleft()
        # 인접한 노드 탐색
        for r_dir, c_dir in dir:
            r, c = row + r_dir, col + c_dir
            # 그래프를 벗어나지 않고, 방문한 적이 없는 칸이면
            if 0 <= r <= (n - 1) and 0 <= c <= (m - 1) and graph[r][c] == 1:
                # 큐에 추가하고 전의 노드값에 +1한 값을 저장한다.
                que.append((r, c))
                graph[r][c] = graph[row][col] + 1

    return graph[n - 1][m - 1]


print(bfs(0, 0))
