class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        location = {}
        result = []

        for index, value in enumerate(nums2):
            location[value] = index

        for i in nums1:
            if i in location:
                result.append(location[i])

        return result