# p.146의 그래프를 BFS함
from collections import deque

que = deque()

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visit = [False] * 9


def bfs(v):
    if len(que) == 0:  # 큐가 비어있는 경우
        return

    for i in graph[que[0]]:
        if not visit[i]:  # 연결된 노드 중 아직 방문하지 않은 노드가 있는 경우
            que.append(i)
            visit[i] = True

    print(que[0], end=" ")
    bfs(que.popleft())


visit[1] = True
que.append(1)
bfs(1)
