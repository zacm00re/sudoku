# Zac moore zmoore4@u.rochester.edu
import sys
import time # one sec per test case
import math

class Sudoku:
    def __init__(self, state_str):
        self.board = state_str.replace("\n", " ").split(" ")
        self.board = [int(x) for x in self.board]
        self.num_rows = int(math.sqrt(len(self.board)))

    def get_column(self, col):
        return [self.board[i] for i in range(col, len(self.board), self.num_rows)]

    def get_row(self, row):
        i = row * self.num_rows
        return self.board[i:i + self.num_rows] #board[i:i+9]
    
    def get_grid(self, grid_index):
        grid_size = int(math.sqrt(self.num_rows))
        start_index = grid_size * grid_index + 2 * self.num_rows * (grid_index // grid_size) # y=3x+18*⌊x/3⌋
        grid = [self.board[start_index + self.num_rows * i : start_index + self.num_rows * i + grid_size] 
            for i in range(grid_size)] # 0+9*i:0+9*i+3
        return [x for row in grid for x in row]

    def validate_board(self):
        # rows
        for i in range(self.num_rows):
            row = self.get_row(i)
            zeroless_row = [x for x in row if x!= 0]
            if len(zeroless_row) != len(set(zeroless_row)):
                return False

        # columns
        for i in range(self.num_rows):
            column = self.get_column(i)
            zeroless_column = [x for x in column if x!= 0]
            # print(zeroless_column)
            if len(zeroless_column) != len(set(zeroless_column)):
                return False

        # grids
        for i in range(self.num_rows):
            grid = self.get_grid(i)
            zeroless_grid = [x for x in grid if x != 0]
            if len(zeroless_grid) != len(set(zeroless_grid)):
                return False

        return True



if __name__ == "__main__":
    state_str = sys.stdin.read().strip()
    s = Sudoku(state_str)
    # print(state_str)  
    print(s.validate_board())
