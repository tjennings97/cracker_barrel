#https://thecleverprogrammer.com/2020/10/04/card-game-with-python/

class Hole:
    def __init__(self, location, state):
        self.location = location
        self.state = state
    def get_state(self):
        return self.state
    def get_location(self):
        return self.location
    def change_state(self):
        self.state = not self.state
	

class Board:
    def __init__(self):
        self.valid_moves = {
            0:[[1,3],[2,5]],
            1:[[3,6],[4,8]],
            2: [[4,7],[5,9]],
            3: [[1,0],[4,5],[6,10],[7,12]],
            4: [[4,11],[8,13]],
            5: [[2,0],[4,3],[8,12],[9,14]],
            6: [[3,1],[7,8]],
            7: [[4,2],[8,9]],
            8: [[4,1],[7,6]],
            9: [[5,2],[8,7]],
            10: [[6,3],[11,12]],
            11: [[7,4],[12,13]],
            12: [[7,3],[8,5],[11,10],[13,14]],
            13: [[8,4],[12,11]],
            14: [[9,5],[13,12]]
        }
        self.holes = []
        self.holes.append(Hole(0, False))
        for i in range(1,15):
            self.holes.append(Hole(i, True))
        self.peg_count = 14
    
    def are_moves(self):
        for hole in self.holes: # loop through holes
            if hole.get_state() is True: # if hole is filled
                moves = self.valid_moves[hole.get_location()] # get valid moves for hole
                for move in moves: # loop through moves for hole
                    if self.holes[move[0]].get_state() is True: # if jumping hole (move[0]) is filled
                        if self.holes[move[1]].get_state() is False: # if landing hole (move[1]) is empty
                            return True # valid move
        return False # no valid moves

    def check_move(self, start, land):
        if start in self.valid_moves:
            if self.holes[start].get_state() is True:
                moves = self.valid_moves[start] # get moves for hole
                for move in moves:
                    if move[1] == land: # if landing hole is valid landing hole given starting hole
                        if self.holes[land].get_state() is False: # if landing hole (move[1]) is empty
                            if self.holes[move[0]].get_state() is True: # if jumping hole (move[0]) is filled
                                return True
        return False # not a valid move

    def decrease_pegs(self):
        self.peg_count = self.peg_count - 1

    def print_board(self):
        icons = []
        '''
        Figure out why this comparison isn't working
        '''
        for hole in self.holes:
            print(hole.get_state())
            if hole.get_state is False:
                icons.append('o')
            else:
                icons.append('*')
        print(f"""
            {icons[0]}
           {icons[1]} {icons[2]}
          {icons[3]} {icons[4]} {icons[5]}
         {icons[6]} {icons[7]} {icons[8]} {icons[9]}
        {icons[10]} {icons[11]} {icons[12]} {icons[13]} {icons[14]}
        """)



class Game:
    def __init__(self):
        self.board = Board()
        self.board.print_board()
    
g = Game()
