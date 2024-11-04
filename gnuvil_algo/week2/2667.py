import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

N = int(input())
graph = []
visited = [[False for _ in range(N)] for _ in range(N)]

dxs = [0, 1,  0, -1]
dys = [1, 0, -1,  0]
result_array = []

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for _ in range(N):
    value = input()
    graph.append(value)

def bfs(new_x, new_y):
    q = deque()
    q.append((new_x, new_y))
    count = 1

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            ndx, nds = x + dx, y + dy

            if in_range(ndx, nds):
                if not visited[ndx][nds] and graph[ndx][nds] == "1":
                    q.append((ndx, nds))
                    visited[ndx][nds] = True
                    count += 1
            
    return count

for i in range(N):
    for j in range(N):
        if int(graph[i][j]) == 1 and not visited[i][j]:
            visited[i][j] = True
            value = bfs(i, j)
            result_array.append(value)
            

print(len(result_array))
result_array.sort()
for result in result_array:
    print(result)

