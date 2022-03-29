def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()

    for i in d:
        answer += i

        if answer > budget:
            break
        cnt += 1
    return cnt