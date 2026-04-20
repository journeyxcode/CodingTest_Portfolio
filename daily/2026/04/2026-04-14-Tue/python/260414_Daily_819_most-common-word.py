"""
╔══════════════════════════════════════════════════════════╗
║  문제명 : Most Common Word (819)
║  플랫폼 : Leetcode
║  분류 : Array, Hash Table, String
║  난이도 : Easy
║  풀이일 : 2026-04-14
║  소요시간 : 30분 이상
║  URL : https://leetcode.com/problems/most-common-word/description/?envType=problem-list-v2&envId=wlzc4tdj
╚══════════════════════════════════════════════════════════╝

[문제]
Given a string paragraph and a string array of the banned words banned, 
return the most frequent word that is not banned. It is guaranteed there is at least 
one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
Note that words can not contain punctuation symbols.

[입출력]
Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a

[접근 방식]
- 정규식 re.sub(r'[^a-z ]', ' ', ...)으로 영문자와 공백을 제외한 모든 문자를
  공백으로 치환하여 구두점을 제거한다. (전처리)
- banned 리스트를 set으로 변환하여 금지어 조회를 O(1)로 최적화한다.
- split()으로 단어를 분리한 뒤, 금지어가 아닌 단어만 dict에 카운트한다.
- max(word_count, key=word_count.get)으로 최대 빈도 단어를 반환한다.

[사용 함수]
- str.lower()        : 대소문자 통일
- re.sub(pattern, repl, string) : 정규식 치환
- set()              : 금지어 조회 O(1) 최적화
- dict.get(key, 기본값)  : 키 없을 때 기본값 반환 (카운트 초기화 간결화)
- max(iterable, key=함수) : key 함수 기준으로 최댓값 반환

[트러블슈팅]
-
- 없음

[시간복잡도]
- O(P + B) : paragraph의 길이를 P, banned의 원소 수를 B라 할 때,
        1) cc.lower()                : O(P)
        2) re.sub(...)               : O(P)
        3) set(banned)               : O(B)
        4) cleaned.split()           : O(P)
        5) 단어별 금지어 체크 + 카운트 : O(P)  (총 단어 수는 최대 P)
        6) max(word_count, ...)      : O(W)  (W = 서로 다른 단어 수, W ≤ P)
        → O(P + B)

[공간복잡도]
- O(P + B) : 
        - cleaned 문자열         : O(P)
        - banned_set             : O(B)
        - word_count 딕셔너리     : O(W), W ≤ P
        → O(P + B)

[개선 여지]
- collections.Counter를 사용하면 카운트 로직을 한 줄로 축약 가능
  예: Counter(word for word in cleaned.split() if word not in banned_set).most_common(1)[0][0]
- 다음번 풀이 시 Counter 버전으로 리팩토링해보기

"""
import re
from typing import List

class Solution:
    def mostCommonWord(self, cc: str, banned: List[str]) -> str:

        cleaned = re.sub(r'[^a-z ]', ' ' ,cc.lower()) # 영문자와 공백 외 모든 문자(구두점 등)를 공백으로 치환
        banned_set = set(banned) # 금지어를 집합으로 변환 (조회 O(1))
        
        word_count = {}
        for word in cleaned.split(): # 금지어를 집합으로 변환 (조회 O(1))
            if word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1 # 금지어가 아닌 단어의 빈도 카운트
        return max(word_count, key=word_count.get) # 최대 빈도 단어 반환