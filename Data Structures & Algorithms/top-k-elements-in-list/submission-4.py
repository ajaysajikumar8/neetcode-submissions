# Top K with sorting (using hashmap)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for item in nums:
            occurences[item] = occurences.get(item, 0) + 1
        
        sorted_array = sorted(occurences, key=lambda x: occurences[x], reverse=True)
        return sorted_array[:k]