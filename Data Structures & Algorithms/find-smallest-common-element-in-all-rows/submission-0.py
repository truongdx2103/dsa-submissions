class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])
        for i in mat[0]:
            isExist = 1
            for j in range(1, r - 1):
                if i not in mat[j]:
                    isExist = 0
                    break
            if isExist == 1:
                return i

        return -1
            