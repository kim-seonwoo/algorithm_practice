import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N+1)

for i in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 순회하면서 가중치 비롯 정보들을 edges 배열에 추가

distance[1] = 0

# 1번째만 거리를 0으로 초기화

for _ in range(N - 1):
    for start, end, time in edges:
        # edges들을 순회하면서, 조건에 맞을 경우 distance[end]를 최신화
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

mCycle = False

for start, end, time in edges:
    # 사이클 여부를 판정
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)

else:
    print(-1)