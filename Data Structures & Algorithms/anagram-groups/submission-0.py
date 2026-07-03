from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)       # khoa (chuoi da sap xep) -> danh sach chuoi
        for s in strs:
            key = ''.join(sorted(s))     # chu ky: 'eat' -> 'aet'
            groups[key].append(s)        # gom chuoi goc vao dung nhom
        return list(groups.values())     # tra ve tat ca cac nhom