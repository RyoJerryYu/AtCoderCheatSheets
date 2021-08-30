import pytest
import heap

@pytest.fixture
def initHeap():
    return heap.Heap([1,3,4,7,2,6,5,9,0,8], 
                     lambda a,b:a>b)

class Test_TestHeap:
    def test_init_notNull(self, initHeap:heap.Heap):
        assert initHeap.size() == 10
        assert initHeap.top() == 9
    
    def test_insert_notTop(self, initHeap:heap.Heap):
        initHeap.insert(6)
        assert initHeap.size() == 11
        assert initHeap.top() == 9
    
    def test_insert_top(self, initHeap:heap.Heap):
        initHeap.insert(10)
        assert initHeap.size() == 11
        assert initHeap.top() == 10
    
    def test_pop(self, initHeap:heap.Heap):
        p = initHeap.pop()
        assert p == 9
        assert initHeap.size() == 9
        assert initHeap.top() == 8