# We compare the length of the set (nums) with the normal nums
# Time complexity: O(n), Space complexity: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)