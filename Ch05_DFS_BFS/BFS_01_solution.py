# 책의 답
from collections import deque

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visit = [False] * 9


def bfs(graph, start, visit):
    que = deque([start])
    visit[start] = True

    while que:  # 큐가 빌 때까지 반복
        v = que.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if visit[i] == False:
                que.append(i)
                visit[i] = True


bfs(graph, 1, visit)
