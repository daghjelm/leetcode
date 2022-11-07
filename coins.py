# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sum = 0
        n = len(coins) - 1
        start = coins[n]
        while start > coins:

        while sum < amount:
        



def main():
    s = Solution()
    coins = [1,2,3]
    amount = 10

if __name__ == '__main__':
    main()
