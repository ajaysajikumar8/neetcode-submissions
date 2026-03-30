class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: 
            return nums
        
        mid = len(nums) // 2
        left_array = self.sortArray(nums[:mid])
        right_array = self.sortArray(nums[mid:])

        return self.merge(left_array, right_array)
        

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        i = 0
        j = 0
        results = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                results.append(left[i])
                i += 1
            else: 
                results.append(right[j])
                j += 1

        results.extend(left[i:])
        results.extend(right[j:])
        return results