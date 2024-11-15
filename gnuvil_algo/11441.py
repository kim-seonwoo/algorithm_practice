import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
pre = [0]
mysum = 0

for i in range(n):
    mysum += nums[i]
    pre.append(mysum)

for i in range(m):
    l, m  = map(int,input().split())
    print(pre[m] - pre[l - 1])
