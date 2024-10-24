class SimpleMap:
    def __init__(self):
        self.items = []

    def set(self, key, value):
        for item in self.items:
            if item[0] == key:  
                item[1] = value
                return
        self.items.append([key, value])

    def get(self, key, default=None):
        for item in self.items:
            if item[0] == key:
                return item[1]
        return default

    def remove(self, key):
        for item in self.items:
            if item[0] == key:
                self.items.remove(item)
                return

    def keys(self):
        return [item[0] for item in self.items]

    def values(self):
        return [item[1] for item in self.items]

    def items(self):
        return self.items

# Example usage:
my_map = SimpleMap()

my_map.set("name", "John")
my_map.set("age", 25)
my_map.set("city", "Example City")

print("Keys:", my_map.keys())
print("Values:", my_map.values())
print("Items:", my_map.items())

# Accessing values by key
print("Name:", my_map.get("name"))
print("Gender:", my_map.get("gender", "Not specified"))

# Removing a key-value pair
my_map.remove("age")

print("Keys after removing 'age':", my_map.keys())

