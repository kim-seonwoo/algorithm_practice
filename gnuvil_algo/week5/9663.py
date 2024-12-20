import sys
input = sys.stdin.readline  

n = int(input())
result_count = 0

# 열과 대각선 방향을 추적하는 배열
columns = [False] * n              # 각 열에 퀸이 있는지 확인
diag1 = [False] * (2 * n - 1)      # / 방향 대각선 (x + y) 특정할수 있는 좌표임
diag2 = [False] * (2 * n - 1)      # \ 방향 대각선 (x - y + n - 1)

def sol(row):
    global result_count
    
    # 종료 조건: 모든 행에 퀸을 배치한 경우
    if row == n:
        result_count += 1
        return
    
    # 현재 행에서 가능한 모든 열에 퀸 배치
    for col in range(n):
        if columns[col] or diag1[row + col] or diag2[row - col + n - 1]:
            continue  # 이미 공격받는 위치는 건너뜀
        
        # 현재 위치에 퀸 배치
        columns[col] = diag1[row + col] = diag2[row - col + n - 1] = True
        sol(row + 1)  # 다음 행으로 진행
        # 백트래킹: 퀸 배치 해제
        columns[col] = diag1[row + col] = diag2[row - col + n - 1] = False

sol(0)
print(result_count)
