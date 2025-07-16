from collections import deque

def BFS(a, vis, st):
    q = deque()
    q.append((st, -1))  
    vis[st] = True

    while q:
        node, p = q.popleft()
        for i in a[node]:
            if not vis[i]:
                vis[i] = True
                q.append((i, node))
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

for st in range(n):
    if not vis[st]:
        if BFS(a, vis, st):
            cycle = True
            break

print("Cycle detected!" if cycle else "No cycle.")
