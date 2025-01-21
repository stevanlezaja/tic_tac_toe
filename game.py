ROW = 3
COL = 3

PLAYERS = ['x', 'o']

class Game:
    def __init__(self):
        self.board = [["I", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        self.current_player = 0
        self.msg = ""
        self.selected = [0, 0]

    def update_board(self, write):
        for i in range(ROW):
            for j in range(COL):
                if self.board[i][j] == 'X':
                    self.board[i][j] = 'x'
                elif self.board[i][j] == 'O':
                    self.board[i][j] = 'o'
                if self.board[i][j] not in PLAYERS:
                    self.board[i][j] = " "
        if write:
            if self.board[self.selected[0]][self.selected[1]] == " ":
                self.board[self.selected[0]][self.selected[1]] = PLAYERS[self.current_player]
                self.current_player = (self.current_player + 1) % 2
                self.msg = f"Player {PLAYERS[self.current_player]}'s turn."
            else:
                self.msg = "Invalid move. Please try another move."
        else:
            if self.board[self.selected[0]][self.selected[1]] == " ":
                self.board[self.selected[0]][self.selected[1]] = "I"
            elif self.board[self.selected[0]][self.selected[1]] == 'x':
                self.board[self.selected[0]][self.selected[1]] = 'X'
            elif self.board[self.selected[0]][self.selected[1]] == 'o':
                self.board[self.selected[0]][self.selected[1]] = 'O'
            


    def get_inputs(self):
        command = input()
        if command == "w":
            self.selected[0] -= 1
            if self.selected[0] < 0:
                self.selected[0] = ROW - 1
        elif command == "s":
            self.selected[0] += 1
            if self.selected[0] == ROW:
                self.selected[0] = 0
        elif command == "a":
            self.selected[1] -= 1
            if self.selected[1] < 0:
                self.selected[1] = COL - 1
        elif command == "d":
            self.selected[1] += 1
            if self.selected[1] == COL:
                self.selected[1] = 0
        elif command == "":
            self.update_board(True)
        self.update_board(False)

    def display_board(self):
        for i in range(ROW):
            for j in range(COL):
                print(self.board[i][j], end='')
                if j < COL - 1:
                    print('|', end='')
            if i < ROW - 1:
                print('\n-+-+-')
        print('\n', self.msg)

    def check_end_condition(self):
        for i in range(ROW):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != " ":
                self.msg = f"Player {self.board[i][0]}'s win!"
                return True
        for j in range(COL):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] != " ":
                self.msg = f"Player {self.board[0][j]}'s win!"
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            self.msg = f"Player {self.board[0][0]}'s win!"
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            self.msg = f"Player {self.board[0][2]}'s win!"
            return True
        if all([self.board[i][j] != " " for i in range(ROW) for j in range(COL)]):
            self.msg = "Draw!"
            return True