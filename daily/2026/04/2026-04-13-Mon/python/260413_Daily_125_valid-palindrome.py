"""
╔══════════════════════════════════════════════════════════╗
║  문제명 : Valid Palindrome (125)
║  플랫폼 : Leetcode
║  분류 : Two Pointers, String
║  난이도 : Easy
║  풀이일 : 2026-04-13
║  소요시간 : 30분 이상
║  URL : https://leetcode.com/problems/valid-palindrome/description/
╚══════════════════════════════════════════════════════════╝

[문제]
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

[입출력]
Example 1:
- Input: s = "A man, a plan, a canal: Panama"
- Output: true
- Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
- Input: s = "race a car"
- Output: false
- Explanation: "raceacar" is not a palindrome.

Example 3:
- Input: s = " "
- Output: true
- Explanation: s is an empty string "" after removing non-alphanumeric characters.
- Since an empty string reads the same forward and backward, it is a palindrome.

[접근 방식]
- 리스트 컴프리헨션으로 문자열을 순회하며 영숫자(isalnum())만 필터링하고, 
  동시에 소문자(lower())로 변환해 정제된 리스트를 만든다.
- 정제된 리스트와 이를 뒤집은 리스트([::-1])를 비교해 동일하면 팰린드롬으로 판정한다.
- 문제 분류는 Two Pointers이지만, 파이썬의 슬라이싱 특성을 활용하면 
  투 포인터를 명시적으로 구현하지 않고도 간결하게 해결 가능하다.
- Two Pointers 방식으로도 풀 수 있음 (다음에 내용추가하기)

[트러블슈팅]
- 없음

[시간복잡도]
- O(N) : 문자열 s의 길이를 N이라 할 때,
        1) 리스트 컴프리헨션 순회: O(N)
        2) cleaned[::-1]로 뒤집기: O(N)
        3) == 비교: 최악의 경우 O(N)
        → O(N) + O(N) + O(N) = O(N)

[공간복잡도]
- O(N) : 정제된 리스트 cleaned가 최대 N개의 문자를 저장하고,
        뒤집힌 리스트 cleaned[::-1]도 추가로 N개를 저장하므로 N에 비례한다.
"""
# ──────────────────────────────────────────────
# 채택 풀이: 리스트 컴프리헨션 (가독성 우선)
# ──────────────────────────────────────────────
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        return cleaned == cleaned[::-1]


# ──────────────────────────────────────────────
# 대안 풀이: Two Pointers (공간복잡도 O(1))
# ──────────────────────────────────────────────
class SolutionTwoPointers:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True