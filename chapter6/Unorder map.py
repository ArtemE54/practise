class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class UnorderedMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return len(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair.key == key:
                pair.value = value
                return
        self.buckets[index].append(KeyValuePair(key, value))

    def get(self, key, default=None):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair.key == key:
                return pair.value
        return default

    def remove(self, key):
        index = self._hash(key)
        self.buckets[index] = [pair for pair in self.buckets[index] if pair.key != key]

    def keys(self):
        return [pair.key for bucket in self.buckets for pair in bucket]

    def values(self):
        return [pair.value for bucket in self.buckets for pair in bucket]

    def items(self):
        return [(pair.key, pair.value) for bucket in self.buckets for pair in bucket]

# Пример использования:
my_map = UnorderedMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())
