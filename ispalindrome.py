class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alf = 'abcdefghijklmnopqrstuvwxyz0123456789'
        new_s = ''
        for c in s:
            if c in alf:
                new_s += c
        a = 0
        b = len(new_s) - 1
        while a < b:
            if new_s[a] != new_s[b]:
                return False
            a += 1
            b -= 1
        return True
