import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline  

a, b, c = map(int, input().split())

# 자연수 A를 B번 곱한 수를 알고 싶다. 
# 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오
# 지수 법칙
# 나머지 분배 법칙 ab곱의 나머지는 a나머지 b나머지의 나머지랑 같다.
def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(multi(a, b))


# 이 문제를 풀때 if n == 1까지 계층적으로 타고 들어가면서 return 을 하면서
# temp에 값을 넣으면서 차근차근히 탈출하면서 나옴
# 