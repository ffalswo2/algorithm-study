def closing(bracket,stack):
    if bracket == ")" and stack[-1] == "(":
        stack.pop()
    elif bracket == "}" and stack[-1] == "{":
        stack.pop()
    elif bracket == "]" and stack[-1] == "[":
        stack.pop()
    else:
        stack.append(bracket)


def solution(s):
    stack = []
    for i in s:
        if stack:
            closing(i,stack)
        else:
            stack.append(i)

    if stack:
        return False
    return True