# 숫자 카드 게임
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

temp = []
for i in range(n):
    temp.append(min(matrix[i]))

result = max(temp)

print(result)
