import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

N, K = map(int, input().split())
dist = [0 for _ in range(100001)]

def bfs(n, k):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            return
        
        if 0 <= 2*x < 100001 and dist[2*x] == 0:
                dist[2*x] = dist[x]
                q.append(2*x)

        for i in [-1, 1]:
            nx = x + i
            if 0 <= nx < 100001 and dist[nx] == 0 :
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs(N, K)