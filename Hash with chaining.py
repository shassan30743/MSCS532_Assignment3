class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash_function(self, key):
        
        return hash(key) % self.size
    
    def insert(self, key, value):
        
        index = self._hash_function(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        self.table[index].append([key, value])
    
    def search(self, key):
        
        index = self._hash_function(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  
    
    def delete(self, key):
        # Find the index using the hash function
        index = self._hash_function(key)
        # Search for the key and remove it from the chain
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False  # Return False if the key doesn't exist

# Example usage
hash_table = HashTable(10)
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
print(hash_table.search("apple"))  # Output: 1
hash_table.delete("apple")
print(hash_table.search("apple"))  # Output: None
