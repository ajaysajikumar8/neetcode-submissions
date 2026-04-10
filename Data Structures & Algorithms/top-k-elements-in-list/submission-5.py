class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums: 
            occurences[num] = occurences.get(num, 0) + 1
        
        

        for elem, freq in occurences.items():
            bucket[freq].append(elem)

        for i in range(len(bucket) -1, 0, -1):
            for j in bucket[i]:
                result.append(j)

            if len(result) == k: 
                return result
