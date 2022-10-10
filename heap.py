import sys
class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = ('1.1.1977', sys.maxsize)
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return (pos-1)//2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2*pos+1

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return 2*pos+2

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if self.hasLeftChild(pos) and self.hasRightChild(pos):
            return False
        return True

    def getParent(self,pos):
        return self.Heap[self.parent(pos)]

    def getLeftChild(self,pos):
        return self.Heap[self.leftChild(pos)]

    def getRightChild(self, pos):
        return self.Heap[self.rightChild(pos)]

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        tmp = self.Heap[fpos]
        self.Heap[fpos] = self.Heap[spos]
        self.Heap[spos] = tmp

    # Function to heapify the node at pos
    def maxHeapify(self,pos):
        smallerChildIndex = pos
        if self.leftChild(pos) < self.size and self.Heap[smallerChildIndex][1] < self.getLeftChild(pos)[1]:
            smallerChildIndex = self.leftChild(pos)
            if self.rightChild(pos) < self.size and self.Heap[smallerChildIndex][1] < self.getRightChild(pos)[1]:
                smallerChildIndex = self.rightChild(pos)
            elif smallerChildIndex != pos:
                self.swap(pos, smallerChildIndex)
                self.maxHeapify(smallerChildIndex)

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size == self.maxsize:
            return
        self.Heap[self.size] = element
        self.size += 1
        current = self.size - 1
        while (self.parent(current) >= 0 and self.getParent(current)[1] < self.Heap[current][1]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
        

    # Function to print the contents of the heap
    def Print(self):

        for i in range(1, (self.size // 2) + 1):
            print(i)
            print("PARENT : " + str(self.Heap[i]) +
                  "LEFT CHILD : " + str(self.Heap[2 * i]) +
                  "RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):
        if self.size == 0:
            raise Exception("Heap is empty")
        data = self.Heap[0]
        self.Heap[0] = self.Heap[self.size-1]
        self.maxHeapify(0)
        self.size -= 1
        date, val = data[0], data[1]
        return "{0},{1}".format(date,val)


# Driver Code
if __name__ == "__main__":
    input = input()
    input = input.split(";")
    dates = []
    values = []
    for d in input:
        date = d.split(',', 2)
        dates.append(date[0])
        values.append(date[2])

    values = [int(x) for x in values]
    tuples = list(zip(dates, values))
    heap = MaxHeap(len(tuples) + 1)
    for t in tuples:
        heap.insert(t)

    print(heap.extractMax())
