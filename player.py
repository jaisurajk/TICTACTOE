import random 
import math

class Player:
    def __init__(self, name, sign):
        self.name = name  
        self.sign = sign  
        self.options = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
        self.othersign = "O" if self.sign == "X" else "X"
        
    def get_sign(self):
        return self.sign
    
    def get_name(self):
        return self.name
    
    def choose(self, board):
        cell = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n")
        if cell in self.options and board.isempty(cell):
            board.set(cell, self.sign)
        else:
            print("You did not choose correctly.")
            print(Player.choose(self, board))
        board.show()   

class AI(Player):
    def __init__(self, name, sign, board):
        Player.__init__(self, name, sign)
        self.board = board
        
    def choose(self, board):
        cell=random.choice(self.options)
        if cell in self.options and board.isempty(cell):
            board.set(cell, self.sign)
        else:
            AI.choose(self, board)
            
    def empty_cells(self, board):
        return [i for i in self.options if board.isempty()]
        
class MiniMax(AI):
    def choose(self, board):
        move = ""
        value = -math.inf
        for i in board.get_options():
            board.set(i, self.sign)
            elo = self.minimax(board, self.othersign)
            board.set(i, " ")
            if elo > value:
                move = i
                value = elo
        board.set(move, self.sign)
        
    def minimax(self, board, sign):
        if board.isdone():
            if board.get_winner() == self.sign:
                return 1
            elif board.get_winner() == "":
                return 0 
            else:
                return -1
            
        if sign == self.sign:
            max_score = -math.inf
            for i in board.get_options():
                board.set(i, self.sign)
                max_score = max(max_score, self.minimax(board, self.othersign))
                board.set(i, " ")
            return max_score
        else:
            min_score = math.inf
            for i in board.get_options():
                board.set(i, self.othersign)
                min_score = min(min_score, self.minimax(board, self.sign))
                board.set(i, " ")
            return min_score  
        
class SmartAI(AI):
    def choose(self, board):
        edges = ['A1', 'A3', 'C1', 'C3']
        mid_sides = ['A2', 'B1', 'B3', 'C2']
        for i in board.get_options():
            board.set(i, self.sign)
            if board.isdone() and board.get_winner() == self.sign:
                return
            board.set(i, " ")
            
        for i in board.get_options():
            board.set(i, self.othersign)
            if board.isdone() and board.get_winner() == self.othersign:
                board.set(i, self.sign)
                return
            board.set(i, " ")
            
        if board.isempty('B2'):
            board.set('B2', self.sign)
            
        while len(edges) > 0:
            cell = random.choice(edges)
            if board.isempty(cell):
                board.set(cell, self.sign)
                return
            else:
                edges.remove(cell)
                
        while len(mid_sides) > 0:
            cell = random.choice(mid_sides)
            if board.isempty(cell):
                board.set(cell, self.sign)
                return
            else:
                mid_sides.remove(cell)