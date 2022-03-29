import heapq


def solution(no, works):
    result = 0
    works = [-i for i in works]

    heapq.heapify(works)

    for i in range(no):
        # 모든 작업을 0으로 만들었음에도 no이 남으면 계속해서 더해지는 예외상황이 존재
        # -> works[0] (가장 큰 값)이 0이 아닐때 조건 추가
        if works[0] != 0:
            task = heapq.heappop(works) + 1
            heapq.heappush(works, task)

    for i in works:
        result += i ** 2

    return result

