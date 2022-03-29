def solution(s):
    answer = 1

    string_list = [s[0]]

    for i in s[1:]:

        if string_list and i == string_list[-1]:
            string_list.pop()
        else:
            string_list.append(i)

    return int(string_list == [])

