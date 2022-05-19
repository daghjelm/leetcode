from time import sleep

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        l = 0
        h = x 

        while l <= h:
            m = (l + h) // 2

            if m * m == x:
                return m
            elif m * m < x:
                if (m + 1) * (m + 1) > x:
                    return m
                else:
                    l = m + 1
            elif m * m > x:
                if (m - 1) * (m - 1) < x:
                    return m - 1
                else:
                    h = m - 1
        
        return m

s = Solution()
print(s.mySqrt(9))
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(25))
print(s.mySqrt(2))
print(s.mySqrt(10))
print(s.mySqrt(1))