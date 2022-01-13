# pos = input()
#
# col = pos[0]
# row = int(pos[1])
#
# if col == 'a':
#     col = 1
# elif col == 'b':
#     col = 2
# elif col == 'c':
#     col = 3
# elif col == 'd':
#     col = 4
# elif col == 'e':
#     col = 5
# elif col == 'f':
#     col = 6
# elif col == 'g':
#     col = 7
# elif col == 'h':
#     col = 8
#
#
# # UL, UR, RU, RD, LU, LD,DL,DR
# dx = [-2,-2,-1,1,-1,1,2,2]
# dy = [-1,1,2,2,-2,-2,-1,1]
#
# cnt = 0
#
# for i in range(8):
#     nx = row + dx[i]
#     ny = col + dy[i]
#
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#     cnt += 1
#
# print(cnt)

data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

cnt = 0

for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]

    if nrow < 1 or ncol < 1 or nrow > 8 or ncol > 8:
        continue

    cnt += 1

print(cnt)