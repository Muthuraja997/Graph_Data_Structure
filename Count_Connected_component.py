n = 8
edges = [
    [0, 1], [1, 2], [2, 0],     
    [3, 4], [4, 5], [5, 3]]
l = set(frozenset([i]) for i in range(n))
for st, en in edges:
    start = end = None
    for comp in l:
        if st in comp:
            start = comp
        if en in comp:
            end = comp
        if start and end:
            break
    if start != end:
        l.remove(start)
        l.remove(end)
        l.add(start.union(end))
print(l,len(l))

for st, en in edges:
    for comp in l:
        if st in comp and en in comp:
            print("YES")
            break
    else:
        continue
    break

print(l) 
print(len(l))