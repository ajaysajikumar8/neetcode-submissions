# Brute force solution

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        for _ in range(k):
            max_count = 0
            max_element = None

            for item in set(nums): 
                if item in result: 
                    continue
                
                count = 0
                for x in nums: 
                    if x == item: 
                        count += 1
                    
                if count > max_count: 
                    max_count = count
                    max_element = item
            result.append(max_element)
        
        return result