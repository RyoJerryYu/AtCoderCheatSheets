from typing import Any, Callable, Generic, List, TypeVar

T = TypeVar("T")

def lfChildOf(i:int):
    return (i + 1) << 1 - 1

def rtChildOf(i:int):
    return (i + 1) << 1

def parentOf(i:int):
    return (i - 1) >> 1

class Heap(Generic[T]):
    def __init__(self, A:List[T]=[], 
                 fCompare:Callable[[T,T],bool]=lambda a,b:a>b
                 ) -> None:
        self.A = A
        self.fCompare = fCompare
        for i in reversed(range(len(A))):
            self.sinkDown(i)
    
    def size(self):
        return len(self.A)
    
    def top(self):
        return self.A[0]
    
    def sinkDown(self, i:int):
        lc = lfChildOf(i)
        rc = rtChildOf(i)

        larger = i
        if lc < self.size() and self.fCompare(self.A[lc], self.A[larger]):
            larger = lc
        if rc < self.size() and self.fCompare(self.A[rc], self.A[larger]):
            larger = rc
        
        if larger == i:
            return
        
        self.A[larger], self.A[i] = self.A[i], self.A[larger]
        self.sinkDown(larger)

    def floatUp(self, i:int):
        if i <= 0:
            return
        
        pr = parentOf(i)
        if self.fCompare(self.A[pr], self.A[i]):
            return
        
        self.A[pr], self.A[i] = self.A[i], self.A[pr]
        self.floatUp(pr)
    
    def insert(self, v:T):
        self.A.append(v)
        self.floatUp(len(self.A) - 1)

    def pop(self)->T:
        res = self.A[0]

        self.A[0] = self.A[len(self.A) - 1]
        self.A.pop()
        self.sinkDown(0)

        return res

