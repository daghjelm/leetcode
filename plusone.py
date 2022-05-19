class Solution:
    def plusOne(self, digits):
        n = len(digits) - 1
        last = digits[n]
        while last == 9:
            digits[n] = 0
            last = digits[n - 1]
            n -= 1
        
        if n < 0:
            digits[0] = 1
            digits.append(0)
        else:
            digits[n] += 1
    
        return digits

if __name__ =='__main__':
    s = Solution()
    print(s.plusOne([1,2,3,4]))
    print(s.plusOne([1,2,3,9]))
    print(s.plusOne([1,2,9,9]))
    print(s.plusOne([9,9,9,9]))