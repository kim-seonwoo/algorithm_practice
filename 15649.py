import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

n, m = map(int, input().split())

seq = []
visited = [0 for _ in range(n + 1)]

def sol(k):

    # 종료 조건
    if k == m:
        for i in seq:
            print(i, end=' ')
        print()

        return

    # 실제 반복문
    for i in range(1, n+1):
        if visited[i]: continue
        # 자릿수를 기록
        visited[i] = 1
        seq.append(i)
        # 다음 스텝으로 가는 재귀적으로 호출
        sol(k + 1)
        # 탈출했을 때 초기화
        visited[i] = 0
        seq.pop()


sol(0)