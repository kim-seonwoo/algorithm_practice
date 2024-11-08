import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10*3)

input = sys.stdin.readline  

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(M):
    i, j = map(int, input().split())
    print(sum(numbers[0:j]) - sum(numbers[0:i - 1]))