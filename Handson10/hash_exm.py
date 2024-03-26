class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * initial_capacity

    def hash(self, key):
        # Multiplication hash function
        A = 0.6180339887  # Multiplicative constant (golden ratio)
        hashed_key = int(self.capacity * (key * A % 1))
        return hashed_key

    def insert(self, key, value):
        index = self.hash(key)
        new_node = Node(key, value)

        if not self.table[index]:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

        if self.size >= self.capacity * 2:
            self.resize(self.capacity * 2)

    def get(self, key):
        index = self.hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self.hash(key)
        current = self.table[index]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

    def resize(self, new_capacity):
        new_table = [None] * new_capacity
        for item in self.table:
            current = item
            while current:
                index = self.hash(current.key)
                if not new_table[index]:
                    new_table[index] = Node(current.key, current.value)
                else:
                    node = new_table[index]
                    while node.next:
                        node = node.next
                    node.next = Node(current.key, current.value)
                current = current.next
        self.capacity = new_capacity
        self.table = new_table

        # Optional: Shrink the table if it becomes too empty
        if self.size <= self.capacity // 4 and self.capacity > 8:
            self.resize(self.capacity // 2)

    def print_table(self):
        for index, item in enumerate(self.table):
            print(f"[{index}]:", end=" ")
            current = item
            while current:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")


# Example usage
ht = HashTable()

# Insert some key-value pairs
ht.insert(1, 10)
ht.insert(2, 20)
ht.insert(3, 30)
ht.insert(4, 40)
ht.insert(5, 50)
ht.insert(6, 60)
ht.insert(7, 70)
ht.insert(8, 80)
ht.insert(9, 90)
ht.insert(10, 100)

# Print the hash table
ht.print_table()

# Retrieve value for a key
print("Value for key 5:", ht.get(5))

# Remove a key-value pair
ht.remove(5)

# Print the updated hash table
ht.print_table()
