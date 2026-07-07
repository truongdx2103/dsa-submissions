class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cal_key = {}
        sum = 0
        for i, v in enumerate(keyboard):
            cal_key[v] = i

        prev = 0
        for i in word:
            sum += abs(cal_key[i] - prev)
            prev = cal_key[i]

        return sum