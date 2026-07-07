class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        real_list = set()
        reject = 0
        for i in emails:
            real_email = ""
            isdomain = 0
            for j in i:
                if j == '+':
                    reject = 1
                    continue
                elif j == '@':
                    reject = 0
                    isdomain = 1
                    continue
                if (ord(j) >= 97 and ord(j) <= 122 and reject == 0) or isdomain == 1:
                        real_email += j
            real_list.add(real_email)

        return len(real_list)