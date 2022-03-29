from collections import deque, Counter
import math


def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    firstTaskDay = days[0]
    for i in range(1, len(days)):
        if days[i] < firstTaskDay:
            days[i] = firstTaskDay
        else:
            firstTaskDay = days[i]
            continue

    answer = list(Counter(days).values())

    return answer

