class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""

      def get_size(self):
            return self.size
             # optional, return the board size (an instance size)

      def get_winner(self):
            return self.winner
            # return the winner's sign O or X (an instance winner)

      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            poss_wins = {'A1': 0, 'A2': 3, 'A3': 6, 'B1': 1, 'B2': 4, 'B3': 7, 'C1': 2, 'C2': 5, 'C3': 8}
            self.board[poss_wins[cell]] = sign
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            poss_wins = {'A1':0, 'A2':3, 'A3':6, 'B1':1, 'B2':4, 'B3':7, 'C1':2, 'C2':5, 'C3':8}
            if self.board[poss_wins[cell]] != ' ':
                return False
            else:
                return True

      def isdone(self):
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X

            #checks wins for vertical
            for i in range(0,3):
                if (self.board[i+6] == self.board[i+3] == self.board[i]) and self.board[i] != ' ':
                    self.winner = self.board[i]
                    return True

            #checks wins for horizontal
            for i in range(0,3):
                if (self.board[3*i+1] == self.board[3*i+2] == self.board[3*i]) and self.board[3*i] != ' ':
                    self.winner = self.board[3*i]
                    return True


            #checks wins for diagonal 1
            if (self.board[8] == self.board[4] == self.board[0]) and self.board[4] != ' ':
                self.winner = self.board[4]
                return True

            #checks wins for diagonal 2
            if (self.board[2] == self.board[4] == self.board[6]) and self.board[4] != ' ':
                self.winner = self.board[4]
                return True

      def show(self):
          #draw the board
          
          print('   A   B   C') 
          print(' +---+---+---+')
          print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
          print(' +---+---+---+')
          print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
          print(' +---+---+---+')
          print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
          print(' +---+---+---+')