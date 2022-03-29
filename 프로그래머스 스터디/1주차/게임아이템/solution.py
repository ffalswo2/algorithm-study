from collections import deque
import heapq


def solution(healths, items):
    answer = []
    heap = []
    # 체력이 적은순으로
    healths.sort()

    # 인덱스를 포함한 아이템 리스트 작성
    items = [(buff, debuff) for buff, debuff in enumerate(items, 1)]
    item_list = deque(sorted(items, key=lambda x: x[1][1]))

    for hp in healths:
        # for문을 통해 index를 구할시 아이템 사용(pop)시에 list길이가 바껴 index error
        # -> enumerate()를 통해 인덱스를 포함한 리스트를 만들어 while문으로 구성
        while item_list:
            idx = item_list[0][0]
            buff = item_list[0][1][0]
            debuff = item_list[0][1][1]

            if hp - debuff < 100:
                break

            # 공격력 가장 높은 것을 찾기위한 우선순위 큐
            heapq.heappush(heap, (-buff, idx))
            # 아이템 사용
            item_list.popleft()

        if heap:
            # 공격력 가장 높은 것의 인덱스 answer에 삽입
            answer.append(heapq.heappop(heap)[1])

    return sorted(answer)