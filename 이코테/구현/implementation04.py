n,m = map(int,input().split())
x,y,direction = map(int,input().split())

# 현재 서있는 위치 방문처리
d = [[0] * m for _ in range(n)]
d[x][y] = 1

# 맵 만들기
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

# N,E,S,W
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turnLimit = 0

while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if arr[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x,y = nx,ny
        cnt += 1
        turnLimit = 0
        continue
    else:
        turnLimit += 1

    if turnLimit == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arr[nx][ny] == 0:
            x,y = nx,ny
        else:
            break

        turnLimit = 0

print(cnt)