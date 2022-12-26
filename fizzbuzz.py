class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [''] * n 
        for i in range(n):
            div3 = (i + 1) % 3 == 0
            div5 = (i + 1) % 5 == 0
            if div3 and div5:
                ans[i] = 'FizzBuzz'
            elif div3:
                ans[i] = 'Fizz'
            elif div5:
                ans[i] = 'Buzz'
            else:
                ans[i] = str(i + 1)
        return ans
            
