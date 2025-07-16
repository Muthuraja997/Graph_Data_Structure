import heapq
class graph:
    def __init__(self):
        self.graph=dict()
    def add_edge_to_graph(self,edge1,edge2,weight):
        if edge1 not in self.graph:
            self.graph[edge1]=[]
        if edge2 not in self.graph:
            self.graph[edge2]=[]
        self.graph[edge1].append((edge2,weight))
        self.graph[edge2].append((edge1,weight))
    def dijikstra_to_find_shortest_path(self,source):
        dis={node:float('inf') for node in self.graph}
        dis[source]=0
        min_heap=[(0,source)]
        while min_heap:
            cur_distance,cur_node=heapq.heappop(min_heap)
            for neig,weight in self.graph[cur_node]:
                distance=cur_distance+weight
                if distance<dis[neig]:
                    dis[neig]=distance
                    heapq.heappush(min_heap,(distance,neig))
        return dis
    def check_shortest_from_source_to(self,source,vis):
        print(vis[source])
        

g1=graph()
for i in range(5):
    st,ed,we=input().split()
    g1.add_edge_to_graph(st,ed,int(we))
vis=g1.dijikstra_to_find_shortest_path('A')
print(vis)
g1.check_shortest_from_source_to('D',vis)