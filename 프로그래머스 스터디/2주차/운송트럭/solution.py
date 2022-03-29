from collections import defaultdict


def solution(max_weight, specs, names):
    answer = 1

    specs_dict = defaultdict(int)
    for name, weight in specs:
        specs_dict[name] = int(weight)

    truck = max_weight
    load = 0
    for name in names:
        load += specs_dict[name]
        if load > max_weight:
            answer += 1
            load = specs_dict[name]

    return answer