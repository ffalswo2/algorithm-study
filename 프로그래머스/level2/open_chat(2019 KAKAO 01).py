def solution(records):
    answer = []
    logs = []
    mp = {}

    for record in records:
        split = record.split(' ')

        if split[0] == "Enter":
            mp[split[1]] = split[2]
            logs.append([split[1], "님이 들어왔습니다."])
        elif split[0] == "Leave":
            logs.append([split[1], "님이 나갔습니다."])
        else:
            mp[split[1]] = split[2]

    for log in logs:
        user_id, string = log[0], log[1]
        answer.append(str(mp[user_id]) + string)

    return answer