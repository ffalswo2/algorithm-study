def solution(monster, S1, S2, S3):
    answer = 0

    monster = set(monster)

    # 몬스터를 만날 확률
    for dice1 in range(1, S1 + 1):
        for dice2 in range(1, S2 + 1):
            for dice3 in range(1, S3 + 1):
                if (1 + dice1 + dice2 + dice3) in monster:  # O(1)
                    answer += 1

    return int((1 - (answer / (S1 * S2 * S3))) * 1000)