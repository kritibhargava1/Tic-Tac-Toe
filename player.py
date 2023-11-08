import random 

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X

      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name

      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n').upper()
                  if cell in valid_choices :
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                        else:
                             print('You did not choose correctly.')
                  else:
                        print('You did not choose correctly.')

class AI(Player):
      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            random_val = random.randint(0,8)
            board.set(random_val, self.sign)
            
                  
class MiniMax(Player):
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        high_score = 0


    def minimax(self, board, self_player):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
        # is a tie
            elif board.get_winner() == "":
                return 0
        # self is a looser (opponent is a winner)
            else:
                return -1

        if self_player:
            high_score = 0
            for i in range(0, len(board.board)):
                if board.board[i] == " ":
                    if self.sign != "X":
                        board.set(i, "X")
                    else:
                        board.set(i, "O")
                    talls = self.minimax(board, True)
                    board.set(i, " ")
            return high_score
                  
