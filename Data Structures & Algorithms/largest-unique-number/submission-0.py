class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        result = -1
        if len(nums) == 1:
            return nums[0]

        for i in nums:
            if i == result:
                result = -1
            elif i > result:
                result = i

        return result