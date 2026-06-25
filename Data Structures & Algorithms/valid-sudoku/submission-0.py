class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_squares = [[set() for _ in range(3)] for _ in range(3)]
        seen_cols = [set() for _ in range(9)]
        print(seen_cols)

        for row in range(9):
            seen_rows = set()
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                if num in seen_rows:
                    return False
                seen_rows.add(num)

                if num in seen_cols[col]:
                    return False
                seen_cols[col].add(num)

                if num in seen_squares[row//3][col//3]:
                    return False
                seen_squares[row//3][col//3].add(num)

        return True
