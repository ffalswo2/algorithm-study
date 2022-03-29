from collections import Counter, defaultdict


def solution(v):
    x_dict = defaultdict(int)
    y_dict = defaultdict(int)

    for x, y in v:
        x_dict[x] += 1
        y_dict[y] += 1

    total = list(x_dict.items()) + list(y_dict.items())

    answer = [num for num, cnt in total if cnt == 1]

    return answer