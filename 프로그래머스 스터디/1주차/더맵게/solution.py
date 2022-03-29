import heapq


# O(n log n)으로 풀어야될듯
def solution(scoville, K):
    mixCnt = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        mixed = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, mixed)
        mixCnt += 1

        # 더이상 섞을 것이 없고 마지막 남은 것이 여전히 K보다 작다면 불가능으로 판단
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return mixCnt
