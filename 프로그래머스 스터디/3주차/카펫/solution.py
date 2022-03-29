import math


def solution(brown, red):
    area_candidate = []

    total = brown + red
    for i in range(1, int(math.sqrt(total)) + 1):
        if total % i == 0:
            area_candidate.append((total // i, i))

    for x, y in area_candidate:
        if (x - 2) * (y - 2) == red:
            return [x, y]