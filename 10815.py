import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
result = [0 for _ in range(m)]
count = -1

def judge(n):
    if n in numbers:
        return True
    else:
        return False

numbers.sort()

for number in arr:
    lo = 0
    hi = n - 1
    count += 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if number <= arr[mid]: 
            hi = mid
        else:
            lo = mid
        if lo == number:
            result[count] = 1
            print(count)



for n in result:
    print(n, end=' ')