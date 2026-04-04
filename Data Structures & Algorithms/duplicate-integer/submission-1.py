class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
                if count > 1:
                    return True

        return False