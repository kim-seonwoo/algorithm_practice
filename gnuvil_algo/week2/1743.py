import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n,m,k = tuple(map(int, input().split()))
graph = [[False for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


for _ in range(k):
    column, row = tuple(map(int, input().split()))
    graph[column - 1][row - 1] = True
    

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs = [0 , 1, 0, -1]
dys = [1, 0, -1, 0]

top_range = 1

def bfs(num_x, num_y):
    q = deque()
    q.append((num_x, num_y)) 
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y):
                if graph[new_x][new_y] == True and not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    count += 1


    return count

for i in range(n):
    for j in range(m):
        if graph[i][j] and visited[i][j] == False:
            visited[i][j] = True   
            count = bfs(i, j)
            if count > top_range:
                top_range = count


print(top_range)
