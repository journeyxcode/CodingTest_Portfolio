"""
╔══════════════════════════════════════════════════════════╗
║  문제명 : Palindrome Linked List (234)
║  플랫폼 : Leetcode
║  분류 : Linked List, Two Pointers, Stack, Recursion
║  난이도 : Easy
║  풀이일 : 2026-04-18
║  소요시간 : 30분 이상
║  URL : https://leetcode.com/problems/palindrome-linked-list/description/
╚══════════════════════════════════════════════════════════╝

[문제]
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

[입출력]
Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false

[접근 방식]
- 연결 리스트를 head부터 순회하며 각 노드의 값을 파이썬 리스트(vals)에 복사한다.
- 복사된 리스트와 그것을 뒤집은 리스트([::-1])를 비교하여 팰린드롬 여부를 판정한다.
- 단일 연결 리스트(singly linked list)는 역방향 탐색이 불가능하므로, 배열로 복사해 슬라이싱 트릭을 활용하는 방식이 가장 간결하다.

[사용 함수]
- list.append(x)      : O(1) 평균 시간에 원소 추가
- list[::-1]          : 새 리스트를 역순으로 복사 (O(N) 시간/공간)
- ==                  : 리스트 요소별 비교 (O(N) 최악)

[트러블슈팅]

- 없음

[시간복잡도]
- O(N) : 연결 리스트의 노드 수를 N이라 할 때,
        1) while 순회하며 append   : O(N)
        2) vals[::-1] 뒤집기        : O(N)
        3) == 비교 (최악)           : O(N)
        → O(N)

[공간복잡도]
- O(N) : 
    - vals 리스트  : O(N)  (노드 값 N개 복사)
    - vals[::-1] : O(N)  (뒤집힌 리스트 추가 생성) → O(N)

[개선 여지]
- 공간복잡도 O(1)로 최적화하려면 "Slow/Fast 포인터 + 후반부 역순" 기법 필요
  1) Slow/Fast 포인터로 중간 지점 찾기
  2) 후반부를 제자리(in-place)에서 뒤집기
  3) 전반부와 뒤집힌 후반부를 비교
- LeetCode Follow-up에서 "O(n) time, O(1) space"를 요구하므로
  면접 대비용으로 반드시 연습해볼 것

"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = [] # 연결 리스트 값을 배열로 복사

        node = head
        while node:
            vals.append(node.val)
            node = node.next

        return vals == vals[::-1] # 배열을 뒤집어 비교