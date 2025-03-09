def is_valid(diagonal, row, col):
    for i in range(row):
        if diagonal[i] == col or \
           diagonal[i] - i == col - row or \
           diagonal[i] + i == col + row:
            return False
    return True
def solve_n_queens(n):
    def solve(row, diagonal):
        if row == n:
            result.append(diagonal[:])
            return
        for col in range(n):
            if is_valid(diagonal, row, col):
                diagonal[row] = col
                solve(row + 1, diagonal)
                diagonal[row] = -1

    result = []
    diagonal = [-1] * n
    solve(0, diagonal)
    return result

def print_solution(solutions):
    for solution in solutions:
        for i in range(len(solution)):
            row = ['.'] * len(solution)
            row[solution[i]] = 'Q'
            print(" ".join(row))
        print("\n")

N = 6
solutions = solve_n_queens(N)
print(f"Number of solutions: {len(solutions)}")
print_solution(solutions)
