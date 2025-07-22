class HashFunction:
    def __init__(self):
        self.size = 5
        self.table = [[] for _ in range(self.size)]

    def insert(self, key, value):
        pos = self.hash_function(key)
        self.table[pos].append(value)

    def hash_function(self, value):
        return value % self.size

hash1 = HashFunction()

for i in range(5):
    a = int(input("Enter key: "))
    b = input("Enter data: ")
    hash1.insert(a, b)

print(hash1.table) 