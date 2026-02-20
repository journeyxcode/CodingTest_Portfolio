"""
╔══════════════════════════════════════════════════════════╗
║  문제명  : 곱셈 (1629)
║  플랫폼  : Baekjoon
║  유형    : 수학, 분할 정복을 이용한 거듭제곱
║  난이도  : 실버 Lv.1
║  풀이일  : 2025-02-16
║  소요시간: 30min
║  URL     : https://www.acmicpc.net/problem/1629
╚══════════════════════════════════════════════════════════╝

[접근 방식]
- input을 호출해 입력 후  값 저장 방식으로 시작 함
- sys.stdin.readline() 방법을 최종 사용
- 거듭제곱과 나머지 출력 방법 사용

[시간복잡도] O(n^2)
[공간복잡도] O(n)

[트러블슈팅]
- 출력 값은 문제가 없으나, 시간초과로 채점이 틀림
- input 입력 후 Output 으로 처리 시간 초과로 문제가 틀림을 확인
"""
import sys

"""
a, b, c = map(int, input().split())
print(f'A : {a}, B : {b}, C : {c}')   # a, b, c 값 출력

step1 = int(a**b)
step2 = step1%c
print(step2)

"""

a, b, c = map(int, sys.stdin.readline().split())

# result = (a**b)%c
# print(result)

# 변수를 사용하지 않고 print에서 호출, 계산
print((a**b)%c)



