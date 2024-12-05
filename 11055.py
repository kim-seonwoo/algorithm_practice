import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n = int(input())
numbers = list(map(int, input().split()))

dp = [-1 for _ in range(n)]

# 어느 부분의 부분 수열합은 최적의 부분 수열합
dp[0] = numbers[0]

for i in range(1, n):
    for j in range(i):
        if numbers[j] < numbers[i]:  
            dp[i] = max(dp[i], dp[j] + numbers[i])



print(max(dp))