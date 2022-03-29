def solution(m, n, puddles):
    # 가로 m  세로 n
    # 위랑 왼쪽 더한 것
    water = 0

    board = [[1] * m for _ in range(n)]
    # 초기 세팅
    for i in range(m):
        board[0][i] = 1
    for i in range(n):
        board[i][0] = 1

    for i in puddles:
        board[i[1] - 1][i[0] - 1] = water

    flag = False
    for i in range(m):
        if flag:
            board[0][i] = water
            continue
        if board[0][i] == water:
            flag = True

    flag = False
    for i in range(n):
        if flag:
            board[i][0] = water
            continue
        if board[i][0] == water:
            flag = True

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == water:
                continue
            board[i][j] = (board[i - 1][j] + board[i][j - 1]) % 1000000007

    return board[n - 1][m - 1]