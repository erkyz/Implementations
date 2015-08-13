from math import floor

# Binary heap with int/float priorities
# (not recursively defined)
class MinHeap: 
    # to allow for O(log n) update, store a hashmap inside heap that maps values to heap indexes
    def __init__(self,items):
        # REQUIRES items is a list of tuples where the first
        # element is the priority and the second element is 
        # the object being stored
        self.heap = [None] # 1-INDEXED
        self.size = 0
        for item in items:
            self.insert(item[0],item[1])

    def siftUp(self,index):
        if index <= 1:
            return
        childIndex = floor(index/2)
        last = self.heap[index]
        parent = self.heap[childIndex]
        if last[0] < parent[0]:
            self.heap[index] = parent
            self.heap[childIndex] = last
            self.siftUp(childIndex)

    def siftDown(self,index):
        if index*2 > self.size:
            return
        leftIndex = index*2
        left = self.heap[leftIndex]
        if leftIndex+1 <= self.size: 
            right = self.heap[leftIndex+1]
        else:
            right = None

        if self.heap[index][0] > left[0] and (right is None or left[0] <= right[0]):
            self.heap[leftIndex] = self.heap[index]
            self.heap[index] = left
            self.siftDown(leftIndex)
        elif right and self.heap[index][0] > right[0] and right[0] < left[0]:
            self.heap[leftIndex+1] = self.heap[index]
            self.heap[index] = right
            self.siftDown(leftIndex+1)

    def insert(self,val,priority):
        # invariant: every level full except last, which is full left-to-right
        # invariant: children all greater than parent
        self.heap.append((priority,val))
        self.size += 1
        self.siftUp(self.size)

    def __delitem__(self,index):
        # REQUIRES index > 0 and index <= self.size
        self.heap[index] = self.heap[-1]
        del self.heap[-1]
        self.size -= 1
        if not index == 1 and self.heap[floor(index/2)][0] > self.heap[index][0]:
            self.siftUp(index)
        else:
            self.siftDown(index)

    def pop(self):
        top = self.heap[1]
        del self[1]
        return top

    def __getitem__(self,index):
        return self.heap[index+1][1] # 0-INDEXED
