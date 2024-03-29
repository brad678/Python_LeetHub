"""
Solution Steps:
1. Build the matrix
"""


class KnightDialer:
    def __init__(self):
        self.next_numbers = { 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [9, 3, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6] }
        
    def bottom_up(self, length: int) -> int:
        dp = [{1: 1} for _ in range(10)]
        
        for length in range(2, length + 1):
            for number in range(10):
                dp[number][length] = sum(dp[next_number][length - 1] for next_number in self.next_numbers[number])
            for number in range(10):
                del dp[number][length - 1]

        return sum(dp[number][length] for number in range(10))  

    def top_down(self, length: int) -> int:
        @cache
        def dp(curr_number: int, length: int) -> int:
            if length == 1:
                return 1
            
            return sum(dp(next_number, length - 1) for next_number in self.next_numbers[curr_number])
        
        return sum(dp(start, length) for start in range(10))   


class Solution:
    def knightDialer(self, n: int) -> int:
        solution = KnightDialer()
        return solution.bottom_up(n) % (10 ** 9 + 7)
        