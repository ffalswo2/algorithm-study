from collections import defaultdict
def solution(seat):

    cinema = set(map(tuple, seat))

    return len(cinema)