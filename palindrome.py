class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        new = 0

        while x > new:
            new = new * 10 + (x % 10)
            x //= 10

        return x == new or x == new // 10

#sol = Solution()
#print(sol.isPalindrome(123))
#print(sol.isPalindrome(12321))
#print(sol.isPalindrome(1221))
#print(sol.isPalindrome(1000001))
#print(sol.isPalindrome(100000))
