class MyHashSet:

    def __init__(self):
        self.data = []
        self.size = 1000000
        i = 0 
        while i <= self.size: 
            self.data.append(False)
            i += 1
        

    def add(self, key: int) -> None:
        self.data[key] = True
        

    def remove(self, key: int) -> None:
        self.data[key] = False
        

    def contains(self, key: int) -> bool:
        if self.data[key]:
            return True
        else: 
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)