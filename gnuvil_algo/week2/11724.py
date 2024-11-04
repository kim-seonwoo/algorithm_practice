import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline  

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
total_count = 0

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        total_count += 1

print(total_count)
