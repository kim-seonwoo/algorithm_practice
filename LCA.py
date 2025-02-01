import sys
import math
sys.setrecursionlimit(10**6)

def dfs(node, depth):
    depths[node] = depth
    for neighbor in tree[node]:
        if depths[neighbor] == -1:
            parent[neighbor][0] = node
            dfs(neighbor, depth + 1)

def preprocess():
    for j in range(1, log_n):
        for i in range(1, n + 1):
            if parent[i][j - 1] != -1:
                parent[i][j] = parent[parent[i][j - 1]][j - 1]

def lca(a, b):
    if depths[a] < depths[b]:  # 항상 a가 더 깊도록
        a, b = b, a

    diff = depths[a] - depths[b]
    for i in range(log_n):
        if diff & (1 << i):
            a = parent[a][i]

    if a == b:
        return a

    for i in range(log_n - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a, b = parent[a][i], parent[b][i]

    return parent[a][0]

n = int(input())  # 노드 개수
tree = {i: [] for i in range(1, n + 1)}
log_n = math.ceil(math.log2(n)) + 1
depths = [-1] * (n + 1)
parent = [[-1] * log_n for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1, 0)
preprocess()

q = int(input())  # 쿼리 개수
for _ in range(q):
    a, b = map(int, input().split())
    print(lca(a, b))
