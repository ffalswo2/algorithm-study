import heapq


def solution(n, works):
    # 최대힙 구성
    works = [-i for i in works]

    heapq.heapify(works)

    for i in range(n):
        if works[0] != 0:
            heapq.heapreplace(works, works[0] + 1)


    return sum([i ** 2 for i in works])