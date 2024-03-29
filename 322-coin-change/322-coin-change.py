class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [inf] * (amount + 1)
        memo[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    memo[i] = min(1 + memo[i - coin], memo[i])

        return -1 if memo[-1] == inf else memo[-1]
            
        