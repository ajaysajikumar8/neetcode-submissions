class MyHashSet:

    def __init__(self):
        self.size = 10007
        self.buckets = []

        i = 0
        while i < self.size: 
            self.buckets.append([])
            i += 1 

    def _hash(self, key: int) -> None:
        return key % self.size 

        

    def add(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        i = 0
        found = False
        while i < len(bucket): 
            if key == bucket[i]: 
                found = True
                break 
            i += 1
        
        if not found: 
            bucket.append(key)


        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        i = 0
        while i < len(bucket):
            if key == bucket[i]: 
                # we found a match - now we remove that by shifting everything left
                j = i
                while j < len(bucket) - 1: 
                    bucket[j] = bucket[j + 1]
                    j += 1
                bucket.pop()
                break

            i += 1


        

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        bucket = self.buckets[index]

        i = 0
        while i < len(bucket):
            if key == bucket[i]:
                return True
            i += 1
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)