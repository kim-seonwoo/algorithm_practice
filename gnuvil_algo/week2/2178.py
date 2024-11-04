import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n, m = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
result_count = 0
queue = deque()

for _ in range(n):
    input_list = []
    input_text = list(map(int,' '.join(input().split())))
    graph.append(input_text)

def defense(x, y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    else:
        return False
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x + dxs[i], y + dys[i]
        if defense(next_x ,next_y):
            if graph[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                graph[next_x][next_y] += graph[x][y]
                queue.append((next_x, next_y))

print(graph[n - 1][m - 1])
