from typing import Dict, List


class UnionFind:
    def __init__(self, N:int) -> None:
        self.N = N
        self.parents = [-1] * N
    
    def find(self, x:int)->int:
        if self.parents[x] < 0:
            return x
        
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x:int, y:int):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        
        if self.parents[xRoot] > self.parents[yRoot]:
            # size(x) < size(y)
            xRoot, yRoot = yRoot, xRoot
        
        self.parents[xRoot] = self.parents[xRoot] + self.parents[yRoot]
        self.parents[yRoot] = xRoot

    def sizeOf(self, x:int):
        return -self.parents[self.find(x)]
    
    def sameAs(self, x:int, y:int):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, p in enumerate(self.parents) if p < 0]
    
    def groupCount(self):
        return len(self.roots())
    
    def members(self, x:int):
        xRoot = self.find(x)
        return [i for i in range(self.N) if self.find(i) == xRoot]

    def all_group_members(self)->Dict[int, List[int]]:
        group_members = {root:[] for root in self.roots()}
        for i in range(self.N):
            group_members[self.find(i)].append(i)
        return group_members
    
    def __repr__(self) -> str:
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())