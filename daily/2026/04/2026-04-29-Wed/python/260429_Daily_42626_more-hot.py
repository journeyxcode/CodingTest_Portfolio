"""
╔══════════════════════════════════════════════════════════╗
║  문제명 : 더 맵게 (42626)
║  플랫폼 : Programmers
║  분류 : 힙(Heap)
║  난이도 : Lv.2
║  풀이일 : 2026-04-29
║  소요시간 : 30분 이상
║  URL : https://school.programmers.co.kr/learn/courses/30/lessons/42626
╚══════════════════════════════════════════════════════════╝

[문제]
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 
아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

[입출력]
| scoville | K | return |
| [1, 2, 3, 9, 10, 12] | 7 | 2 |

- 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

- 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.

[접근 방식]
- 매 연산마다 가장 작은 두 값이 필요 → 최소 힙 사용
- heapify로 변환하면 heappop() 할 때마다 자동으로 최솟값이 나옴
- 최솟값(heap[0])이 K 이상이 되면 모든 값이 K 이상임이 보장되므로 종료
- 음식이 1개만 남았는데 K 미만이면 불가능하므로 -1 반환

[트러블슈팅]
- 매번 sort()로 정렬하면 시간초과 발생 → heapq로 해결
- scoville 원본 보호를 위해 [:]로 복사 후 heapify 적용

[시간복잡도]
- O(n log n)
  - heapify : O(n)
  - while 루프 최대 n번 * heappop/heappush O(log n) = O(n log n)

[공간복잡도]
- O(n) : 힙 저장을 위한 리스트 크기 n

[힙 주요 함수]
heapq.heapify(heap)           # 리스트 → 최소 힙 변환
heapq.heappop(heap)           # 최솟값 꺼내기
heapq.heappush(heap, x)       # 값 삽입
heap[0]                       # 최솟값 조회 (제거 없이)
heapq.nsmallest(n, heap)      # 작은 값 n개 반환
heapq.nlargest(n, heap)       # 큰 값 n개 반환
최대 힙 → 값에 음수 부호(-) 붙여서 사용

"""
import heapq
def solution(scoville, K):    
    heap = scoville[:]
    heapq.heapify(heap)
    answer = 0
    
    while(heap[0] < K):
        if(len(heap)) < 2:
            return -1
        
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        mixed = first + (second*2)
        heapq.heappush(heap, mixed)
        answer += 1
        
    return answer