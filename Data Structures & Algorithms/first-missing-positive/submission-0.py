class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = set()
        min = -1
        for i in nums:
            if i + 1 > 0 and (i + 1 < min or min == -1) and i + 1 not in nums:
                min = i + 1
        return min