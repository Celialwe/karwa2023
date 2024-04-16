n = int(input())
depart = input()

lines = {}
for _ in range(n):
    g1, g2 = input().split()
    if g1 not in lines:
        lines[g1] = [g2]
    else :
        lines[g1].append(g2)
    if g2 not in lines:
        lines[g2] = [g1]
    else :
        lines[g2].append(g1)

poss = lines[depart]
AllSet = {}
visited = {line : False for line in lines}


def dfs(graph, start, visited):
    for v in graph[start]:
        if v not in visited:
            visited[v]
            dfs(graph, v, visited)

dfs(lines, depart, visited)
if any(not visited[v] for v in visited):
    print("impossible")
else:
    if ()
