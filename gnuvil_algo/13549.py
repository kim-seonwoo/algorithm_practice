import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

N, K = map(int, input().split())
dist = [0 for _ in range(100001)]

# bfs 를 구현해서 탐색, 2*X 조건도 매번 탐색함을 추가

def bfs(n, k):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k or 2*x == k:
            print(dist[x])
            return
        for i in [-1, 1]:
            nx = x + i
            if nx == 0:
                nx = x + 1
                q.append(nx)

bfs(N, K)