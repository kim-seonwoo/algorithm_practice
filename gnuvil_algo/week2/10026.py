import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n = int(input())
graph = []
visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [0 , 1, 0, -1]
dys = [1, 0, -1, 0]
colors = ["R", "G", "B"]
result_count = 0

for _ in range(n):
    array = list(input())
    graph.append(array)

def bfs(num_x, num_y):
    visited[num_x][num_y] = True
    color = graph[num_x][num_y]
    q = deque()
    q.append((num_x, num_y)) 
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y):
                if graph[new_x][new_y] == color and not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i, j)
            result_count += 1

print(result_count)

result_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i, j)
            result_count += 1

print(result_count)