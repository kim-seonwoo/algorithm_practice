import sys
sys.setrecursionlimit(10**6)

def dfs(node, dist):
    global farthest, max_dist
    if dist > max_dist:
        farthest, max_dist = node, dist
    for neighbor, weight in tree[node]:
        if visited[neighbor] == 0:
            visited[neighbor] = 1
            dfs(neighbor, dist + weight)

n = int(input())  # 트리의 노드 개수
tree = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):
    u, v, w = map(int, input().split())  # 노드 u-v, 가중치 w
    tree[u].append((v, w))
    tree[v].append((u, w))

# 1차 DFS: 임의의 노드(1)에서 가장 먼 노드 찾기
visited = [0] * (n + 1)
visited[1] = 1
farthest, max_dist = 1, 0
dfs(1, 0)

# 2차 DFS: farthest 노드에서 가장 먼 노드 찾기
visited = [0] * (n + 1)
visited[farthest] = 1
max_dist = 0
dfs(farthest, 0)

print(max_dist)  # 트리의 지름
