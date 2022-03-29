from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(image, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        row, col = queue.popleft()

        for r, c in direction:
            next_row = row + r
            next_col = col + c
            if 0 <= next_row < len(image) and 0 <= next_col < len(image[0]) and not visited[next_row][next_col] and \
                    image[next_row][next_col] == image[row][col]:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col))


def solution(n, m, image):
    answer = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):

            if not visited[i][j]:
                bfs(image, (i, j), visited)
                answer += 1

    return answer