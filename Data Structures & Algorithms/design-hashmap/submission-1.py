# Using direct addressing

class MyHashMap:

    def __init__(self):
        self.size = 1000001
        self.buckets = [-1] * self.size

    def _hash(self, key: int) -> None: 
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        self.buckets[index] = value        
        

    def get(self, key: int) -> int:
        index = self._hash(key)
        return self.buckets[index]
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.buckets[index] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)