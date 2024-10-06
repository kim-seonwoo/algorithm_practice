import sys
sys.stdin = open('input.txt', 'r')

num = int(input())
result = 0

for i in range(num):
    result = 0 
    for j in str(i):
        result += int(j)
    if result + i == num:
        print(i)
        break

if result + i != num:
    print(0)
