class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if self.is_empty():
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        return self.heap[0] if not self.is_empty() else None

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if (self.max_heap and self.heap[index] > self.heap[parent_index]) or \
               (not self.max_heap and self.heap[index] < self.heap[parent_index]):
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            largest_or_smallest = index
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            
            if left_index < len(self.heap) and \
               ((self.max_heap and self.heap[left_index] > self.heap[largest_or_smallest]) or 
                (not self.max_heap and self.heap[left_index] < self.heap[largest_or_smallest])):
                largest_or_smallest = left_index

            if right_index < len(self.heap) and \
               ((self.max_heap and self.heap[right_index] > self.heap[largest_or_smallest]) or 
                (not self.max_heap and self.heap[right_index] < self.heap[largest_or_smallest])):
                largest_or_smallest = right_index

            if largest_or_smallest != index:
                self.heap[index], self.heap[largest_or_smallest] = self.heap[largest_or_smallest], self.heap[index]
                index = largest_or_smallest
            else:
                break

# Пример использования
h = Heap(max_heap=True)  # Создаем максимальную кучу

# Вставка элементов
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)

print("Корень кучи:", h.peek())  # Ожидаемый вывод: 20

# Извлечение корней
while not h.is_empty():
    print("Извлеченный элемент:", h.extract())
