# Brute Force Solution - Selection Sort
# swap using index - swap after inner loop (when finds the shortest_num in the entire inner list)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums