def draw(key):
    for i in range(len(key)):
        for j in range(len(key)):
            print(key[i][j], end=' ')
        print()


def rotate(key):
    copy = [[0] * len(key) for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key)):
            copy[j][len(key) - i - 1] = key[i][j]

    return copy


def unlock_check(board, lock, lock_margin):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if board[lock_margin + i][lock_margin + j] != 1:
                return False
    return True


def solution(key, lock):
    lock_margin = len(key) - 1
    max_length = 58  # 최대치 20 20 20, 거기에 겹쳐있어야하는 부분 최소 한곳은 존재 : -1 두번

    for i in range(lock_margin + len(lock)):
        for j in range(lock_margin + len(lock)):
            # 회전 4번
            for _ in range(4):
                board = [[0] * max_length for _ in range(max_length)]

                # lock 배치
                for l in range(len(lock)):
                    for k in range(len(lock)):
                        board[lock_margin + l][lock_margin + k] = lock[l][k]

                # key 배치
                for kl in range(len(key)):
                    for kj in range(len(key)):
                        board[i + kl][j + kj] += key[kl][kj]

                # unlock 확인
                if unlock_check(board, lock, lock_margin):
                    return True
                key = rotate(key)

    return False