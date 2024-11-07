import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

F, S, G, U, D = map(int, input().split())
dist = [0 for _ in range(F + 1)]

def bfs(vertex, dest, up, down):
    q = deque()
    q.append(vertex)
    options = [up, -down]
    dist[vertex] = 1
    while q:
        x = q.popleft()
        if x == dest :
            print(dist[x] - 1)
            return
        for i in options:
            nx = x + i
            if 1 <= nx <= F:
                if dist[nx] == 0:
                    dist[nx] = dist[x] + 1
                    q.append(nx)

    print("use the stairs")


bfs(S, G, U, D)