class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

        
    def find(self, x,):
        if self.parent[x] == x:
            return x
        else: 
            return self.find(self.parent[x])
        
    def union(self, x, y):
        py = self.find(y)
        px = self.find(x)

        if(py == px):
            return False
        self.parent[px] = py
        return True



def kruskal(edges, num_of_verts):
    edges.sort()
    total = 0
    mst = []
    uf = UnionFind(num_of_verts)
    for edge in edges:
        if uf.find(edge[1]) == uf.find(edge[2]):
            continue
        else: 
            uf.union(edge[1], edge[2])
            mst.append([edge[1], edge[2]])
            total = total + edge[0]
    return mst, total
    