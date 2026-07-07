class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in nums:
            if i + 1 > 0 and i + 1 not in nums:
                return i + 1