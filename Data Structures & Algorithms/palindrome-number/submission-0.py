class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        left, right = 0, len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1

        return True