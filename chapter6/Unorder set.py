class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):
        return hash(value) % self.size

    def add(self, value):
        index = self._hash(value)
        if value not in self.buckets[index]:
            self.buckets[index].append(value)

    def remove(self, value):
        index = self._hash(value)
        if value in self.buckets[index]:
            self.buckets[index].remove(value)

    def contains(self, value):
        index = self._hash(value)
        return value in self.buckets[index]

    def elements(self):
        return {value for bucket in self.buckets for value in bucket}

# Пример использования:
my_set = UnorderedSet()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Elements:", my_set.elements())

value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")

value_to_remove = 1
my_set.remove(value_to_remove)

print("Elements after removing 1:", my_set.elements())
