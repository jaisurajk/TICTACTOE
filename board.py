class Board:
    def __init__(self):
        self.options = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
        self.sign = " "
        self.size = 3
        self.board = list(" " * self.size**2)
        self.winner = ""
        
    def get_size(self): 
        return self.size
    
    def set_winner(self, sign):
        self.winner = sign
        
    def get_winner(self):
        return self.winner 
    
    def set_options(self, cell, value):
        self.options[self.options.index(cell)] = value
        
    def get_options(self):
        return [self.options[i] for i in range(len(self.options)) if self.board[i] == " "]
    
    def set(self, cell, sign):
        self.board[self.options.index(cell)] = sign
        
    def isempty(self, cell):
        if self.board[self.options.index(cell)] == " ":
            return True
        return False
    
    def isdone(self):
        done = False
        self.winner = ''
        if self.board[0] != " " and self.board[0] == self.board[1] == self.board[2]:
            done = True
            self.winner = self.board[0]
        elif self.board[3] != ' ' and self.board[3] == self.board[4] == self.board[5]:
            done = True
            self.winner = self.board[3]
        elif self.board[6] != ' ' and self.board[6] == self.board[7] == self.board[8]:
            done = True 
            self.winner = self.board[6]
        elif self.board[0] != ' ' and self.board[0] == self.board[3] == self.board[6]:
            done = True
            self.winner = self.board[0]
        elif self.board[1] != ' ' and self.board[1] == self.board[4] == self.board[7]:
            done = True
            self.winner = self.board[1]
        elif self.board[2] != ' ' and self.board[2] == self.board[5] == self.board[8]:
            done = True
            self.winner = self.board[2]
        elif self.board[0] != ' ' and self.board[0] == self.board[4] == self.board[8]:
            done = True
            self.winner = self.board[0]
        elif self.board[2] != ' ' and self.board[2] == self.board[4] == self.board[6]:
            done = True
            self.winner = self.board[2]
        elif " " not in self.board:
            done = True
        return done
    
    def show(self):
        print("   A   B   C")
        row1 = "1| {} | {} | {} |".format(self.board[0], self.board[1], self.board[2])
        row2 = "2| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5])
        row3 = "3| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8])
        print(" +---+---+---+")
        print(row1)
        print(" +---+---+---+")
        print(row2)
        print(" +---+---+---+")
        print(row3)
        print(" +---+---+---+")