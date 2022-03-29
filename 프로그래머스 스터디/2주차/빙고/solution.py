from collections import defaultdict


def diagonol1(board, num_dict):
    # bingo = 0

    i = 0
    cnt = 0
    for b in board:
        if i == len(board):
            break
        if num_dict[b[i]] != 0:
            cnt += 1
        i += 1

    # if cnt == len(board):
    #     bingo += 1
    return int(cnt == len(board))
    # return bingo


def diagonol2(board, num_dict):
    # bingo = 0

    i = len(board) - 1
    cnt = 0
    for b in board:
        if i < 0:
            break
        if num_dict[b[i]] != 0:
            cnt += 1
        i -= 1

    # if cnt == len(board):
    #     bingo += 1
    return int(cnt == len(board))
    # return bingo


def vertical(board, num_dict):
    bingo = 0

    for i in range(len(board)):
        cnt = 0
        for b in board:
            if num_dict[b[i]] != 0:
                cnt += 1

        if cnt == len(board):
            bingo += 1

    return bingo


def horizon(board, num_dict):
    bingo = 0
    for line in board:
        cnt = 0
        for num in line:
            if num_dict[num] != 0:
                cnt += 1

        if cnt == len(board):
            bingo += 1

    return bingo


def solution(board, nums):
    answer = 0

    num_dict = defaultdict(int)
    for num in nums:
        num_dict[num] += 1

    answer += horizon(board, num_dict)
    answer += vertical(board, num_dict)
    answer += diagonol1(board, num_dict)  # \
    answer += diagonol2(board, num_dict)  # /

    return answer