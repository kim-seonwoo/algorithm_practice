import sys
sys.stdin = open('input.txt', 'r')

a, b = tuple(map(int, input().split()))
array = list(map(int, input().split()))
result = []

for i in array:
    if i < b:
        result.append(i)

print(*result)