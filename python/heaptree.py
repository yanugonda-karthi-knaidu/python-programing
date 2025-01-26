class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def delete(self, key):
        try:
            index = self.heap.index(key)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            self._bubble_down(index)
        except ValueError:
            print(f"Element {key} not found in heap.")

    def _bubble_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def display(self):
        print("Min Heap:", self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def delete(self, key):
        try:
            index = self.heap.index(key)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            self._bubble_down(index)
        except ValueError:
            print(f"Element {key} not found in heap.")

    def _bubble_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)

    def display(self):
        print("Max Heap:", self.heap)


# Example Usage
if __name__ == "__main__":
    min_heap = MinHeap()
    max_heap = MaxHeap()

    # Inserting elements into MinHeap
    for num in [5, 3, 8, 1, 2]:
        min_heap.insert(num)
    min_heap.display()

    # Deleting an element from MinHeap
    min_heap.delete(3)
    min_heap.display()

    # Inserting elements into MaxHeap
    for num in [5, 3, 8, 1, 2]:
        max_heap.insert(num)
    max_heap.display()

    # Deleting an element from MaxHeap
    max_heap.delete(5)
    max_heap.display()