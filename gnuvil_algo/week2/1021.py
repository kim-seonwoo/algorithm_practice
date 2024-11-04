import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

num_t = int(input())

dxs = [0, 1,  0, -1]
dys = [1, 0, -1,  0]

def in_range(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

def bfs(m, n, graph, visited, q):
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y, m, n) and graph[new_x][new_y] == 1 and not visited[new_x][new_y]:
                q.append((new_x, new_y))
                visited[new_x][new_y] = True

for _ in range(num_t):
    result_count = 0
    m, n, k = tuple(map(int, input().split()))
    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = deque()

    for _ in range(k):
        row, column = tuple(map(int, input().split()))
        graph[row][column] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                result_count += 1
                q.append((i, j))
                visited[i][j] = True  
                bfs(m, n, graph, visited, q)

    print(result_count)
