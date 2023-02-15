# 큰 수의 법칙
def solution():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0

    arr.sort(reverse=True)  # 리턴값 없음. 배열 정렬됨.

    for _ in range(m // (k + 1)):
        for _ in range(k):
            result += arr[0]
        result += arr[1]

    for _ in range(m % (k + 1)):
        result += arr[0]

    return result


print(solution())
