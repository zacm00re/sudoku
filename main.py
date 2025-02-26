# Zac moore zmoore4@u.rochester.edu
import sys
import time # one sec per test case
import math

class Sudoku:
    def __init__(self, state_str):
        self.board = state_str.replace("\n", " ").split(" ")
        self.num_rows = math.sqrt(len(self.board))

    def get_column(self, col):
        return [self.board[i] for i in range(col, len(self.board), self.num_rows)]

    def get_row(self, row):
        i = row * num_rows
        return self.board[i:i+num_rows] #board[i:i+9]

    def validate_board(self):
        # rows
        for i in range(0, num_rows):
            row = get_row(i)
            zeroless_row = [x for x in row if x!= 0]
            if len(zeroless_row) != len(set(zeroless_row)):
                return False

        # columns
        for i in range(0, num_rows):
            column = get_column(i)
            zeroless_column = [x for x in row if x!= 0]
            if len(zeroless_column) != len(set(zeroless_column)):
                return False



if __name__ == "__main__":
    state_str = sys.stdin.read().strip()
    s = Sudoku(state_str)
    print(s.board)  