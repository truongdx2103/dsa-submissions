class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {}

        for i in range(len(s)):
            if s[i] in map:
                if t[i] != map[s[i]]:
                    return False
            else:
                map[s[i]] = t[i]

        return True