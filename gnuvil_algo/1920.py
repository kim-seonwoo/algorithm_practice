import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n = int(input())
a = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
result = []

a.sort()

for target in numbers:
    lo = -1
    hi = n-1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if target > a[mid]:
            lo = mid
        else:
            hi = mid

    if target == a[hi]:
        result.append(1)
    else:
        result.append(0)

for n in result:
    print(n)