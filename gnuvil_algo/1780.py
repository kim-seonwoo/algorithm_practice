import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result0 = 0
result1 = 0
result2 = 0

def allTheSame(y, x, sz):
    base = graph[y][x]
    for i in range(sz):
        for j in range(sz):
            if graph[y + i][x + j] != base:
                return False
    return True

def solve(y, x, sz):
    global result0, result1, result2

    if allTheSame(y, x, sz):
        if graph[y][x] == -1:
            result0 += 1
        elif graph[y][x] == 0:
            result1 += 1
        elif graph[y][x] == 1:
            result2 += 1
        return

    new_sz = sz // 3
    for i in range(3):
        for j in range(3):
            solve(y + i * new_sz, x + j * new_sz, new_sz)

solve(0, 0, n)

print(result0)
print(result1)
print(result2)
