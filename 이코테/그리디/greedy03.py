n,m = map(int,input().split())
# data = []
#
# ans = []
# for i in range(n):
#     l = list(map(int,input().split()))
#     data.append(l)
#     ans.append(min(l))
#
# print(max(ans))

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    result = max(min(data),result)

print(result)