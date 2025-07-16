def DFS(a, p, st, vis):
    vis[st] = True
    for i in a[st]:
        if not vis[i]:
            if DFS(a, st, i, vis):
                return True
        elif i != p:
            return True
    return False

n = 4
edges = [
    [0, 1],
    [1, 2],
    [2, 0],
    [2, 3]
]


a = [[] for _ in range(n)]
for u, v in edges:
    a[u].append(v)
    a[v].append(u)  
    
vis = [False] * n
cycle = False
for i in range(n):
    if not vis[i]:
        if DFS(a, -1, i, vis):
            cycle = True
            break

print("Cycle detected!" if cycle else "No cycle.")
