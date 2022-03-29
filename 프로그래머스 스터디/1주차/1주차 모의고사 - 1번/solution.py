from collections import deque

ill = 0
normal = -1
vaccinated = -2


def bfs(office, queue):
    m = len(office)
    n = len(office[0])

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        y, x = queue.popleft()

        for ny, nx in direction:
            next_y = y + ny
            next_x = x + nx

            if 1 <= next_x < n and 1 <= next_y < m and office[next_y][next_x] == normal:
                office[next_y][next_x] = office[y][x] + 1
                queue.append((next_y, next_x))


def solution(m, n, infests, vaccinateds):
    answer = 0
    queue = deque()
    office = [[normal] * (n + 1) for _ in range(m + 1)]

    for i in infests:
        office[i[0]][i[1]] = ill

    for v in vaccinateds:
        office[v[0]][v[1]] = vaccinated

    queue.extend(map(tuple, infests))

    bfs(office, queue)

    for i in range(1, m + 1):
        if normal in office[i][1:]:
            return -1
        else:
            answer = max(answer, max(office[i][1:]))

    return answer