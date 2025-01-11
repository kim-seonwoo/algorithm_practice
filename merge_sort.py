import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):
    if e - s < 1: return

    m = int(s + (e - s)/ 2) 
    # 중간점
    merge_sort(s, m)
    merge_sort(m + 1, e)
    # 절반으로 나눠 재귀적으로 실행
    for i in range(s, e + 1):
        tmp[i] = A[i]
    # tmp 배열에 값 복사
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1

        else:
            A[k] = tmp[index1]
            k += 1
            index += 1 

    while index1 <= m:
        # 한 쪽 그룹이 모두 선택된 후 남아 있는 값 정리
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1