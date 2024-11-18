import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n, k = map(int, input().split())


array = [0 for _ in range(100001)]

def bfs(vertex):
    q = deque([vertex])
    while q:
        vertex = q.popleft()
        if vertex == k:
            return array[vertex]
        for next_v in (vertex - 1 , vertex+1, 2*vertex):
            if 0 <= next_v < 100001 and not array[next_v]:
                array[next_v] = array[vertex] + 1
                q.append(next_v)

print(bfs(n))