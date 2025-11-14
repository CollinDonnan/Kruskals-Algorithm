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
        self.parent[px] = py

    