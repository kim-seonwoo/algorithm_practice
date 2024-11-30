import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
result = []

numbers.sort()



for target in arr:
    lo = -1
    hi = n - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if numbers[mid] < target:  
            lo = mid    
        else:  
            hi = mid
    
    if numbers[hi] == target:
        result.append(1)
    else:
        result.append(0)
    

print(" ".join(map(str, result)))