import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]  
visited = [False] * (n + 1)  
result_array = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for adj in graph:
    adj.sort()

def dfs(graph, v, visited):
    visited[v] = True
    result_array.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        result = q.popleft()
        result_array.append(result)
        for i in graph[result]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

visited = [False] * (n + 1)
result_array = []
dfs(graph, v, visited)
print(" ".join(map(str, result_array)))
visited = [False] * (n + 1)
result_array = []
bfs(graph, v, visited)
print(" ".join(map(str, result_array)))
