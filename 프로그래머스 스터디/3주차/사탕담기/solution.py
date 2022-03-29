from itertools import combinations


def solution(m, weights):
    answer = 0

    weights = sorted([w for w in weights if w <= m])

    for pick in range(1, len(weights) + 1):
        comb = list(combinations(weights, pick))
        for c in comb:
            if sum(c) == m:
                answer += 1

    return answer