class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        temp = set()

        for i in s:
            if i in temp:
                temp.remove(i)
            else:
                temp.add(i)
            
        return len(temp) < 2