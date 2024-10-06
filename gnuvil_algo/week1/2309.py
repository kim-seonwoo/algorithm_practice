import sys
sys.stdin = open('input.txt', 'r')

arrs = []

for i in range(9):
    person = int(input())
    arrs.append(person)

for person in arrs:
    arrs.remove(person)
    for person2 in arrs:
        arrs.remove(person2)
        if sum(arrs) == 100:
            break
        arrs.append(person2)
    if sum(arrs) == 100:
        break
    arrs.append(person)

arrs.sort() 
print(arrs)