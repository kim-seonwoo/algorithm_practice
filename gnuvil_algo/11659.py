import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10*3)

input = sys.stdin.readline  

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
pre = [0]
mysum = 0

for i in range(N):
    mysum += numbers[i]
    pre.append(mysum)


for _ in range(M):
    i, j = map(int, input().split())
    print(pre[j] - pre[i - 1])