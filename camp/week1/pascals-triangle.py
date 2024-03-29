class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1], [1, 1]]        
        for row in range(3, numRows + 1):
            new_level = [1,]
            
            for col in range(1, row - 1):
                value = rows[-1][col]
                value += 0 if col - 1 < 0 else rows[-1][col - 1]
                new_level.append(value)
            
            new_level.append(1)
            rows.append(new_level)
        
        return rows[:numRows]
        