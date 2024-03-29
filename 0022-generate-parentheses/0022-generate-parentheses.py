class Solution:
    def backtrack(self, opening_left, closing_left, curr):
        if not opening_left and not closing_left:
            self.parentheses.append(curr)

        if not curr or opening_left:
            self.backtrack(opening_left - 1, closing_left, curr + '(')
        if opening_left < closing_left:
            self.backtrack(opening_left, closing_left - 1, curr + ')')
            
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.parentheses = []
        
        self.backtrack(n, n, "")
        
        return self.parentheses
        