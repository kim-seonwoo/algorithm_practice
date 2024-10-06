import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
b = int(input())
c = int(input())

result_num = a * b * c
array = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in str(result_num):
    array[int(i)] += 1

for i in array:
    print(i)