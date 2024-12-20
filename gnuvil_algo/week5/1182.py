import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [0 for _ in range(n)]
seq = []

count = 0

def sol(k):
    global count

    if k == n:

        return

    for i in range(n):
        if visited[i]: continue

        visited[i] = 1
        seq.append(i)

        if sum(seq) == s:
            count += 1

        sol(k + 1)

        visited[i] = 0
        seq.pop()


    


sol(0)

print(count)


