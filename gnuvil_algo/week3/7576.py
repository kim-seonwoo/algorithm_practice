import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dxs = [1, 0 ,-1, 0]
dys = [0, 1, 0, -1]

def bfs(graph):
    result = 0

    q = deque()
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                q.append((i, j)) 

    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x, new_y = x + dxs[i], y + dys[i]
            if 0<= new_x < m and 0 <= new_y < n:
                if graph[new_x][new_y] == 0 and graph[new_x][new_y] != -1:
                    q.append((new_x, new_y))
                    graph[new_x][new_y] = graph[x][y] + 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] > result :
                result = graph[i][j]

    return result


print(bfs(graph))
