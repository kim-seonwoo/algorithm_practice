
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n = int(input())

dxs = [-2, -1, 1, 2, -2, -1, 1, 2]
dys = [1, 2, 2, 1, -1, -2, -2, -1]

def cal():
    k = int(input())
    start_x, start_y = map(int, input().split())
    arr_x, arr_y = map(int, input().split())
    bfs(start_x, start_y, arr_x, arr_y, k)

def bfs(start_x, start_y, dep_x, dep_y, k):
    visited = [[0 for _ in range(k)] for _ in range(k)]
    q = deque()
    count = 0
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()

        if x == dep_x and y == dep_y:
            print(visited[x][y])
            return
        
        for i in range(8):
            nx = x + dxs[i]
            ny = y + dys[i]

            if 0 <= nx < k and 0 <= ny < k:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


for _ in range(n):
    cal()