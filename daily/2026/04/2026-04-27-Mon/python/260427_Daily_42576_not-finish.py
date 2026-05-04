"""
╔══════════════════════════════════════════════════════════╗
║  문제명 : 완주하지 못한 선수 (42576)
║  플랫폼 : Programmers
║  분류 : 해시
║  난이도 : Lv.1
║  풀이일 : 2026-04-27
║  소요시간 : 30분 이상
║  URL : https://school.programmers.co.kr/learn/courses/30/lessons/42576
╚══════════════════════════════════════════════════════════╝

[문제]
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 
담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

[입출력]
| participant | completion | return |
| ["leo", "kiki", "eden"] | ["eden", "kiki"] | "leo" |
| ["marina", "josipa", "nikola", "vinko", "filipa"] | ["josipa", "filipa", "marina", "nikola"] | "vinko" |
| ["mislav", "stanko", "mislav", "ana"] | ["stanko", "ana", "mislav"] | "mislav" |

- "leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
- "vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
- "mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.

[접근 방식]
- 방법 1: 정렬(Sort) + zip 비교
  participant와 completion을 각각 정렬한 뒤, zip으로 묶어 앞에서부터 하나씩 비교한다.
  정렬 후에는 같은 인덱스에 같은 이름이 와야 하므로, 처음으로 다른 이름이 나오는 지점이 완주하지 못한 선수다.
  모든 쌍이 일치하면 participant의 마지막 원소가 완주하지 못한 선수다.

- 방법 2: collections.Counter 차집합
  Counter로 각 배열의 이름 빈도수를 구한 뒤, participant Counter에서 completion Counter를 빼면
  완주하지 못한 선수만 남는다. (Counter 빼기는 결과가 0 이하인 키를 자동으로 제거한다.)

- 방법 3: 딕셔너리 수동 카운팅
  딕셔너리에 participant의 각 이름 빈도수를 직접 기록하고,
  completion을 순회하며 해당 이름의 카운트를 1씩 차감한다.
  최종적으로 카운트가 1 이상인 이름이 완주하지 못한 선수다. 

[트러블슈팅]
- 풀이방법이 생각나지 않았음
  → 동명이인 케이스 ("mislav"가 2명) 때문에 단순 집합(set) 차이로는 풀 수 없다.
     빈도수 기반으로 접근해야 한다는 점을 인식하는 것이 핵심이다.
  → 방법 1의 정렬+zip 아이디어는 "정렬하면 같은 위치에 같은 이름이 와야 한다"는
     직관에서 출발하면 떠올리기 쉽다.


[시간복잡도]
- 방법 1: O(N log N) — sort가 지배 (zip 비교는 O(N))
- 방법 2: O(N) — Counter 생성 O(N) + 차집합 O(N)
- 방법 3: O(N) — 딕셔너리 순회 두 번 (participant, completion 각 O(N))

[공간복잡도]
- 방법 1: O(N) — sort는 Timsort 기준 최대 O(N)의 추가 메모리 사용
- 방법 2: O(N) — 두 Counter 객체 저장
- 방법 3: O(N) — 딕셔너리 count 저장

zip과 딕셔너리 위키 : https://wikidocs.net/92539
counter 위키 : https://wikidocs.net/233689

"""
# 방법 1
def solution(participant, completion):    
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

# 방법 2
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

# 방법 3
def solution(participant, completion):    
    count = {}
    
    for p in participant:
        count[p] = count.get(p, 0) + 1 
    
    for c in completion:
        count[c] -= 1
        
    for name, cnt in count.items():
        if cnt > 0:
            return name

