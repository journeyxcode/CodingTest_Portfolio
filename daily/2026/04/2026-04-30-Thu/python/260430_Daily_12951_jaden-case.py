"""
╔══════════════════════════════════════════════════════════╗
║  문제명 : JadenCase 문자열 만들기 (12951)
║  플랫폼 : Programmers
║  분류 : 연습문제
║  난이도 : Lv.2
║  풀이일 : 2026-04-30
║  소요시간 : 30분 이상
║  URL : https://school.programmers.co.kr/learn/courses/30/lessons/12951
╚══════════════════════════════════════════════════════════╝

[문제]
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

[입출력]
| s | return |
| "3people unFollowed me" | "3people Unfollowed Me" |
| "for the last week" | "For The Last Week" |

[접근 방식]
- split() 대신 문자 단위 순회를 선택
  → split()은 연속 공백을 무시해 원본 공백 구조를 복원할 수 없음
- "직전 문자가 공백인가?"만 추적하면 단어 시작 위치를 판별 가능
- prev = " " 로 초기화하여 첫 글자를 별도 처리 없이 자연스럽게 대문자 처리
- 숫자에 upper()/lower()를 적용해도 변화 없으므로 별도 분기 불필요

[트러블슈팅]
- 연속 공백 처리: split() 사용 시 "hello  world" → ["hello", "world"]로
  공백 개수 정보가 손실됨. 문자 순회 방식은 공백도 result에 그대로 추가하므로
  연속 공백이 자동으로 보존됨
- 대소문자 혼재 입력(unFollowed): 무조건 lower() 처리로 통일되어 자동 해결

[시간복잡도]
- O(n) : 문자열 s를 한 번만 순회

[공간복잡도]
- O(n) : 결과 문자열 result가 입력 크기에 비례해 증가

"""
def solution(s):
    result = ""
    prev = " "  # 시작은 공백으로 간주

    for char in s:
        if prev == " ":
            result += char.upper()  # 단어 첫 글자 → 대문자
        else:
            result += char.lower()  # 나머지 → 소문자
        prev = char

    return result