# import sys
# sys.stdin = open('input.txt', 'r')

count = input()
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))