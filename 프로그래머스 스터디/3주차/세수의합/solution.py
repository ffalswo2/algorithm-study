import math


def solution(n):
    array = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    result = []
    for i in range(2, len(array)):
        if array[i]:
            result.append(i)

    answer = 0
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            for k in range(j + 1, len(result)):
                if result[i] + result[j] + result[k] == n:
                    answer += 1

    return answer