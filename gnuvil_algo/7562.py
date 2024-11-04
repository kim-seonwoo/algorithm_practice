
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n = int(input().split())

dxs = []
dys = []

def cal():
    k = int(input().split())
    start_x, start_y = map(int, input().split())
    dep_x, dep_y = map(int, input().split())
    visited = [[False for _ in range(k)] for _ in range(k)]
    bfs(start_x, start_y, dep_x, dep_y, k, visited)

for _ in range(n):
    cal()

def bfs(start_x, start_y, dep_x, dep_y, k, visited):
    q = deque()
    while q:
        x, y = q.popleft
        if 0 <= x <= k and 0 <= y <= k:
            if not visited[x][y]:
                visited[x][y] = True
                count += 1
                q.append((x, y))

    print(count)
