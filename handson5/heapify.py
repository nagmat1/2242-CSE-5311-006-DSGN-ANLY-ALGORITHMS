class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def build_min_heap(self, array):
        self.heap = array[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def pop_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.min_heapify(0)
        return root

    def get_root(self):
        return self.heap[0] if self.heap else None

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)


# Example Usage:
if __name__ == "__main__":
    # Example with integers
    min_heap_int = MinHeap()
    min_heap_int.build_min_heap([4, 10, 3, 5, 1])
    print("Min Heap (Integers):", min_heap_int.heap)
    print("Root Node:", min_heap_int.get_root())
    print("Popping Root:", min_heap_int.pop_root())
    print("Min Heap after popping root:", min_heap_int.heap)

    # Example with floats
    min_heap_float = MinHeap()
    min_heap_float.build_min_heap([3.14, 2.718, 1.618, 0.577, 2.302])
    print("\nMin Heap (Floats):", min_heap_float.heap)
    print("Root Node:", min_heap_float.get_root())
    print("Popping Root:", min_heap_float.pop_root())
    print("Min Heap after popping root:", min_heap_float.heap)

    # Example with custom objects
    class CustomObject:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return self.value < other.value

    min_heap_custom = MinHeap()
    objects = [CustomObject(5), CustomObject(2), CustomObject(8), CustomObject(1), CustomObject(4)]
    min_heap_custom.build_min_heap(objects)
    print("\nMin Heap (Custom Objects):", [obj.value for obj in min_heap_custom.heap])
    print("Root Node:", min_heap_custom.get_root().value)
    print("Popping Root:", min_heap_custom.pop_root().value)
    print("Min Heap after popping root:", [obj.value for obj in min_heap_custom.heap])
