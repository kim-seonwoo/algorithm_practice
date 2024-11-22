import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n = int(input())
user_numbers = list(map(int, input().split()))
m = int(input())
provided_numbers = list(map(int, input().split()))

result = [0 for _ in range(m)]

provided_numbers.sort()

for target in user_numbers:
    lo = -1
    hi = m - 1
    while lo + 1 < hi :
        mid = (lo + hi) // 2
        if provided_numbers[mid] > target:
            hi = mid
        else:
            lo = mid
    if provided_numbers[lo] == target:
        result[lo] += 1



print(result)
