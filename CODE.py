class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key already exists, update the value
                self.values[index] = value
                return
            # Linear probing to find the next empty slot
            index = (index + 1) % self.size
        # Found an empty slot, insert the key and value
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key found, return the corresponding value
                return self.values[index]
            # Linear probing to search for the key
            index = (index + 1) % self.size
        # Key not found
        return None

# Example usage
if __name__ == "__main__":
    phone_book = HashTable(10)  # Create a hash table of size 10

    # Inserting clients into the phone book
    phone_book.insert("Alice", "123-456-7890")
    phone_book.insert("Bob", "234-567-8901")
    phone_book.insert("Charlie", "345-678-9012")

    # Looking up telephone numbers
    print(phone_book.get("Alice"))  # Output: 123-456-7890
    print(phone_book.get("Bob"))    # Output: 234-567-8901
    print(phone_book.get("David"))  # Output: None (David is not in the phone book)
