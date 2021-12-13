#https://thecleverprogrammer.com/2020/10/04/card-game-with-python/

class Hole:
    def __init__(self, location, state, color):
        self.location = location
        self.state = state
        self.color = color
    def get_state(self):
        return self.state
    def change_state(self):
        self.state = not self.state
    def get_color(self):
        return self.color
    def change_color(self, color):
        self.color = color
    def get_location(self):
        return self.location
    def set_location(self, new_location):
        self.location = new_location

class Board:
    def __init__(self):
        # come up with formula - reference chess implementations?
        self.valid_moves = {
            0:[[1,3],[2,5]],
            1:[[3,6],[4,8]],
            2: [[4,7],[5,9]],
            3: [[1,0],[4,5],[6,10],[7,12]],
            4: [[7,11],[8,13]],
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
        self.holes.append(Hole(0, False, (0,0,0)))
        temp = [(0, 255, 255),(255,255,255),(255, 0, 0),(255, 255, 0),(0, 255, 255),(255,255,255),(255, 0, 0),(255, 255, 0),(0, 255, 255),(255,255,255),(255, 0, 0),(255, 255, 0),(0, 255, 255),(255,255,255)]
        for i in range(1,15):
            self.holes.append(Hole(i, True, temp[i-1]))
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
            if self.holes[start].get_state() is True: #if starting hole is filled
                moves = self.valid_moves[start] # get moves for hole
                for move in moves:
                    if move[1] == land: # if landing hole is valid landing hole given starting hole
                        if self.holes[land].get_state() is False: # if landing hole (move[1]) is empty
                            if self.holes[move[0]].get_state() is True: # if jumping hole (move[0]) is filled
                                return move[0]
        return -1 # not a valid move
    
    def get_peg_count(self):
        return self.peg_count

    def decrease_pegs(self):
        self.peg_count = self.peg_count - 1

    def print_board(self):
        icons = []
        for hole in self.holes:
            if hole.get_state() == True:
                icons.append('*')
            else:
                icons.append('o')
        print(f"""
            {icons[0]}\t\t\t      0
           {icons[1]} {icons[2]}\t\t\t     1  2
          {icons[3]} {icons[4]} {icons[5]}\t\t\t   3  4  5
         {icons[6]} {icons[7]} {icons[8]} {icons[9]}\t\t  6  7  8  9
        {icons[10]} {icons[11]} {icons[12]} {icons[13]} {icons[14]}\t\t10 11 12 13 14
        """)

class Game:
    def __init__(self):
        self.board = Board()
        self.pointer = 0
        self.pointer_color = (255, 0, 0)
    
    def print_instructions(self):
        print("""
        HOW TO PLAY
        -----------
        You will jump one peg over another to an open
        space, provided that there is a peg in the hole
        between the two locations. You may only jump one
        peg at a time and jumps may only happen along the
        same row or the same diagonal. The peg that was 
        jumped will be removed. You will continue this 
        process until there is only 1 peg left or until 
        there are no remaining moves.

        This game will display two boards. The board on
        the left will be your playing board. This board
        will represent whether holes are filled with a peg,
        using '*,' or empty, using 'o.' The board on the
        right is your reference board. This board shows
        the numbers that represent the holes on the playing
        board.

        For example, the playing board will start a triangle 
        with a 'o' at the top. According to the reference 
        board, this space is represented by 0.

        Leave only 1 - you're genius.
        Leave 2 pegs and you're pretty smart.
        Leave 3 pegs and you are just plain dumb.
        Leave 4 or mor'n you're just plain "EQ-NO-RA-MOOOSE."
        """)
    
    def jump(self, starting_hole, jumped_hole, landing_hole):
        self.board.holes[landing_hole].change_state()
        self.board.holes[landing_hole].change_color(self.board.holes[starting_hole].color)
        self.board.holes[starting_hole].change_state()
        self.board.holes[starting_hole].change_color((0,0,0))
        self.board.holes[jumped_hole].change_state()
        self.board.holes[jumped_hole].change_color((0,0,0))
        self.board.decrease_pegs()

    def print_result(self):
        pegs = self.board.get_peg_count()
        print("Remaining Pegs: " + str(pegs))
        if pegs == 1:
            print("YOU'RE GENIUS")
        elif pegs == 2:
            print("YOU'RE PRETTY SMART")
        elif pegs == 3:
            print("YOU'RE JUST PLAIN DUMB")
        elif pegs > 3:
            print("YOU'RE JUST PLAIN \"EG-NO-RA-MOOSE\"")
        else:
            print("Something went wrong.")
        self.board.print_board()

    
    def play_game(self):
        self.print_instructions()

        play = True
        while play is True:
            self.board.print_board()

            starting_hole = int(input("Jumping peg: "))
            landing_hole = int(input("Landing space: "))
            jumped_hole = self.board.check_move(starting_hole, landing_hole)

            if jumped_hole == -1:
                print("This is an invalid move. Please try again.")
            else:
                self.jump(starting_hole, jumped_hole, landing_hole)
            play = self.board.are_moves()
        
        self.print_result()
        self.board.print_board()

if __name__ == "__main__":
    g = Game()
    g.play_game()
