class Solution:
    def countElements(self, arr: List[int]) -> int:
        temp = set(arr)
        count = 0

        for i in arr:
            if (i + 1) in temp:
                count += 1

        return count