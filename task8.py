def solve_n_queens(n=4):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            # Convert board to solution format and add to results
            solution = [''.join('Q' if cell == 1 else '.' for cell in r) for r in board]
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0  # backtrack

    board = [[0]*n for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions


if __name__ == "__main__":
    solutions = solve_n_queens(n=4)
    print(f"Number of solutions: {len(solutions)}\n")
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
        print()
