class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for item in nums:
            occurences[item] = occurences.get(item, 0) + 1
        
        # how do i sort the dict by desc values though ? and how to get \
        # the k number of occurences of the same / 

        sorted_array = sorted(occurences, key=lambda x: occurences[x], reverse=True)
        return sorted_array[:k]