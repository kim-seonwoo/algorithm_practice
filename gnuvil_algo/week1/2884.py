import sys
sys.stdin = open('input.txt', 'r')

hour, minute = tuple(map(int, input().split()))

if minute < 45 :
    if hour == 0:
        hour = 23
    else:
        hour -= 1
    minute = 60 - 45 + minute

else :
    minute -= 40

print(hour, minute)