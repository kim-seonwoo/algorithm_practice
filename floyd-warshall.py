import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
distance = [[sys.maxsize for j in range(N + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    distance[i][j] = 0

# 인접행렬 초기화

# 노선 데이터를 distance 행렬에 저장
for i in range(M):
    s, e, v= map(int, input().split())
    if distance[s][e] > v:
        distance[s][e] = v

# 플로이드 워셜 수행
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

# 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if distance[i][j] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(distance[i][j], end = ' ')
    print()