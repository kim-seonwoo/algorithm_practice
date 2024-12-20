import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n, m = map(int, input().split())
chars = list(input().split())

visited = [0 for _ in range(n)]
seq = []

chars.sort()

vowel = ['a', 'e', 'i', 'o', 'u']

def check(arr):
    v_count, c_count = 0, 0 # 모음 개수, 자음 개수

    for i in arr:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False

def sol(k, index):
    if k == n:
        if check(seq):
            for s in seq:
                print(s, end='')
            print()
            return
    
    for i in range(n):
        if visited[i]: continue
        # if seq != [] 

        visited[i] = 1
        seq.append(chars[i])

        sol(k + 1, i)

        visited[i] = 0
        seq.pop()


sol(0, 0)
