# Brute Force - Selection Sort 
# Swap each time on the inner loop - inefficient

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): 
            shortest_num = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] < shortest_num: 
                    shortest_num = nums[j]
                    nums[j] = nums[i]
                    nums[i] = shortest_num
        return nums