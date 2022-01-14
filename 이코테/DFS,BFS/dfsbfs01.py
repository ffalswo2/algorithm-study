n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 연결된 모든 노드 방문처리하는 목적으로 수행되는 과정
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        # 방문처리를 하고 True return
        return True
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i,j)
            answer += 1

print(answer)


