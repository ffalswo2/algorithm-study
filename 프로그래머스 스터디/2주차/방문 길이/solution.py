def solution(dirs):
    coord_dict = {}

    cur_y = 0
    cur_x = 0

    for dir in dirs:
        if dir == "U" and cur_y < 5:
            # (현재 좌표, 이동할 좌표)
            coord_dict[(cur_y, cur_x, cur_y + 1, cur_x)] = True
            cur_y += 1

        if dir == "D" and cur_y > -5:
            # (이동할 좌표, 현재 좌표)
            coord_dict[(cur_y - 1, cur_x, cur_y, cur_x)] = True
            cur_y -= 1

        if dir == "L" and cur_x > -5:
            # (현재 좌표, 이동할 좌표)
            coord_dict[(cur_y, cur_x, cur_y, cur_x - 1)] = True
            cur_x -= 1

        if dir == "R" and cur_x < 5:
            # (이동할 좌표, 현재 좌표)
            coord_dict[(cur_y, cur_x + 1, cur_y, cur_x)] = True
            cur_x += 1

    return len(coord_dict)