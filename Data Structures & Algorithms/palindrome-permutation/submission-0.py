class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        temp = []

        for i in s:
            if i in temp:
                temp.remove(i)
            else:
                temp.append(i)
            
        return len(temp) < 2