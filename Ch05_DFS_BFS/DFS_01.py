# p.137의 그래프를 DFS함
if __name__ == "__main__":
    # 인접 리스트 사용
    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
    stack = []
    visit_node = []
    not_visit = []

    # 초기 노드 설정, 방문 처리(graph에서 지움), 스택에 넣음
    node = 1
    stack.append(node)
    visit_node.append(1)

    while True:
        if not stack:
            # Stack이 비었을 경우 while문 나간다
            break

        print(stack)
        top_node = stack[-1]

        not_visit = set(graph[top_node]) - set(visit_node)
        not_visit = list(not_visit)
        not_visit.sort()

        # 스택의 최상단 노드와 인접한 노드가 있을 경우 스택에 넣고 방문 처리.
        if not_visit:  # 두 집합의 차집합이 존재할 때
            linked_node = not_visit[0]
            # 스택에 넣음
            stack.append(linked_node)
            # 방문처리함
            visit_node.append(linked_node)

        # 스택의 최상단 노드와 인접한 노드가 없는 경우 스택에서 pop()한다.
        else:
            stack.pop()
            print(top_node, " pop!")

    print("탐색된 순으로 출력됨.")
    print(visit_node)


#
