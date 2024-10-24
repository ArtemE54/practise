class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        while self.slots[hash_value] not in (None, key):
            hash_value = (hash_value + 1) % self.size
        self.slots[hash_value] = key
        self.data[hash_value] = value

    def get(self, key, default=None):
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                return self.data[hash_value]
            hash_value = (hash_value + 1) % self.size
        return default

    def remove(self, key):
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                self.slots[hash_value] = None
                self.data[hash_value] = None
                return
            hash_value = (hash_value + 1) % self.size

    def keys(self):
        return [key for key in self.slots if key is not None]

    def values(self):
        return [value for value in self.data if value is not None]

    def items(self):
        return [(self.slots[i], self.data[i]) for i in range(self.size) if self.slots[i] is not None]

# Пример использования 
my_hashmap = HashMap() 
my_hashmap.put("name", "John") 
my_hashmap.put("age", 25) 
my_hashmap.put("city", "Example City") 

print("Keys:", my_hashmap.keys())  # Ожидаемый вывод: Keys: ['name', 'age', 'city'] 
print("Values:", my_hashmap.values())  # Ожидаемый вывод: Values: ['John', 25, 'Example City'] 
print("Items:", my_hashmap.items())  # Ожидаемый вывод: Items: [('name', 'John'), ('age', 25), ('city', 'Example City')] 

# Доступ к значениям по ключу 
print("Name:", my_hashmap.get("name"))  # Ожидаемый вывод: Name: John
print("Gender:", my_hashmap.get("gender", "Not specified"))  # Ожидаемый вывод: Gender: Not specified 

# Удаление пары ключ-значение 
my_hashmap.remove("age") 
print("Keys after removing 'age':", my_hashmap.keys())  # Ожидаемый вывод: Keys after removing 'age': ['name', 'city']
