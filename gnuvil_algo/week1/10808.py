import sys
sys.stdin = open('input.txt', 'r')

n = input()
lst = [0]*26 


for i in n:
    lst[ord(i)-97] += 1
    
for i in lst:
    print(i, end=' ')