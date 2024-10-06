
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
count = 0

for i in numbers:
    search = target - i
    for n in numbers:
        if n == search:
            count += 1

print(count)