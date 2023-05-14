import random

class Tiktactoe:
    def __init__(self):
        self.board = list()
        self.current_player = "O"
        self.create_board()

    def create_board(self):
        self.board = [["-", "-", "-"] for _ in range(0,3)]


    def is_cell_taken(self, row, col):
        if self.board[row][col] == "-":
            return False
        else:
            return True

    def is_board_occupied(self):
        occupied = True
        for row in range(0,3):
            for col in range(0,3):
                if self.board[row][col] == "-":
                    occupied = False
        return occupied

    def win(self):
        win_status = False
        player = self.current_player
        #check all rows:
        for row in self.board:
            if row == [player, player, player]:
                win_status = True
        # check all columns:
        for col in range(0,3):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                win_status = True

        # check diagonals:
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
                win_status = True
        elif self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            win_status = True
        return win_status

    def print_board(self):
        str_join_map = "\n".join(map("|".join, self.board))
        print(f"{str_join_map}")

    def first_turn(self):
        first_turn = random.randint(0,1)
        if first_turn == 0:
            self.current_player = "X"
        else:
            self.current_player = "O"

    def mark_spot(self, row, col):
        if self.is_cell_taken(row, col):
            print("the spot is taken. try again")
            row, col = list(map(int, input("Enter row and column numbers to mark your spot: ").split()))
            self.mark_spot(row,col)
        else:
            self.board[row][col] = self.current_player


    def switch_player(self):
        if self.current_player == "O":
            self.current_player = "X"
        else:
            self.current_player = "O"











