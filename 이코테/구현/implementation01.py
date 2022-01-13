# n = int(input())
# data = list(input().split())
#
# x = 1
# y = 1
#
# for i in data:
#
#     if i == 'R':
#         if y == n:
#             continue
#         y += 1
#
#     elif i == "L":
#         if y == 1:
#             continue
#         y -= 1
#     elif i == "U":
#         if x == 1:
#             continue
#         x -= 1
#     elif i == "D":
#         if x == 5:
#             continue
#         x += 1
#
# print(x,y)

# re

n = int(input())
data = list(input().split())

x = 1
y = 1

# L, R, U, D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ["L","R","U","D"]

for i in data:

    for j in range(4):
        if i == move[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x,y = nx,ny


print(x,y)