# Using set with early exit - when duplicate found
# Time complexity: O(n) and space complexity: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False