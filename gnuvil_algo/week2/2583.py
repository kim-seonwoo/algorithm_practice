

# 직사각형 입력 받기, graph 선언
# bfs로 방문 처리, 갈곳 없으면 toss
# local_count와 result_couts 필요

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n,m,k = tuple(map(int, input().split()))
graph = [[False for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
restult_array = []

def visit_rectangle(left_x, left_y, right_x, right_y):
    for i in range(left_x, right_x):
        for j in range(left_y, right_y):
            graph[j][i] = True

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for _ in range(k):
    left_x, left_y, right_x, right_y = tuple(map(int, input().split()))
    visit_rectangle(left_x, left_y, right_x, right_y)

dxs = [0 , 1, 0, -1]
dys = [1, 0, -1, 0]

def bfs(num_x, num_y):
    graph[num_x][num_y] = True
    q = deque()
    q.append((num_x, num_y)) 
    count = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y):
                if graph[new_x][new_y] == False and not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    count += 1

    return count

for i in range(n):
    for j in range(m):
        if not graph[i][j] and visited[i][j] == False:

            local_count = bfs(i, j)
            restult_array.append(local_count)


print(len(restult_array))
restult_array.sort()
for result in restult_array:
    print(result)
