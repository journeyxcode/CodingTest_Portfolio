"""
╔══════════════════════════════════════════════════════════╗
║  문제명 : Palindrome Number (9)
║  플랫폼 : Leetcode
║  분류 : Math
║  난이도 : Easy
║  풀이일 : 2026-04-19
║  소요시간 : 30분 이상
║  URL : https://leetcode.com/problems/palindrome-number/description/?envType=problem-list-v2&envId=wlzc4tdj
╚══════════════════════════════════════════════════════════╝

[문제]
Given an integer x, return true if x is a palindrome, and false otherwise.

[입출력]
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

[접근 방식]
- 음수는 맨 앞에 '-' 부호가 있어 절대 팰린드롬이 될 수 없으므로 조기 반환(early return).
- 정수를 문자열로 변환한 뒤 슬라이싱([::-1])으로 뒤집는다.
- 뒤집은 문자열을 다시 정수로 변환해 원본과 비교한다.
- 분류는 Math이지만, 문자열 변환을 활용하면 간결하게 해결 가능하다.

[사용 함수]
- str(int)           : 정수를 문자열로 변환 (O(log₁₀ x) = O(N), N은 자릿수)
- str[::-1]          : 문자열을 역순으로 복사 (O(N))
- int(str)           : 문자열을 정수로 변환 (O(N))
- ==                 : 정수 비교 (O(1) - 고정 크기로 간주)

[트러블슈팅]
- 없음

[시간복잡도]
- O(N) : 정수 x의 자릿수를 N이라 할 때 (N = log₁₀ x),
1) str(x)         : O(N)
2) [::-1]         : O(N)
3) int(reverse_num) : O(N)
4) == 비교        : O(1)
→ O(N)

[공간복잡도]
- O(N) :
    - str(x)         : O(N)
    - reverse_num    : O(N)
    → O(N)

[개선 여지]
- Follow-up: "Could you solve it without converting the integer to a string?"
  → 수학적 접근으로 절반만 뒤집어 비교하면 O(1) 공간 가능
  
  def isPalindrome(self, x: int) -> bool:
      if x < 0 or (x % 10 == 0 and x != 0):
          return False
      reverted = 0
      while x > reverted:
          reverted = reverted * 10 + x % 10
          x //= 10
      # 자릿수 홀/짝 모두 처리: 홀수 자리면 가운데 숫자 제거
      return x == reverted or x == reverted // 10
      
- 다음 리팩토링 시 수학적 접근 버전 추가 연습

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse_num = str(x)[::-1]

        return x == int(reverse_num)