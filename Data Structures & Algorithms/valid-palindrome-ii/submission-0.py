class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right] and s[left + 1] != s[right] and s[left] != s[right -1]:
                return False
            left += 1
            right -= 1

        return True