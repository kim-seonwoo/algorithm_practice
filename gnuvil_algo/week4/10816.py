import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n = int(input())
user_numbers = list(map(int, input().split()))
m = int(input())
provided_numbers = list(map(int, input().split()))

number_count = {num: 0 for num in provided_numbers}

sorted_keys = sorted(number_count.keys())

for target in user_numbers:
    lo = -1
    hi = m - 1

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if sorted_keys[mid] < target:
            lo = mid
        else:
            hi = mid

    if sorted_keys[hi] == target:
        number_count[sorted_keys[hi]] += 1

result = [number_count[num] for num in provided_numbers]

print(" ".join(map(str, result)))
