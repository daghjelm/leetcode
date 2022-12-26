class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_prof = 0
        for n in prices:
            curr_prof = n - curr_min
            if curr_prof > max_prof:
                max_prof = curr_prof
            if n < curr_min:
                curr_min = n
            
        return max_prof
