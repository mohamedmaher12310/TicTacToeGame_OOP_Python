class GameBoard:
    def __init__(self, cells, current_winner='None'):
        self.cells = cells
        self.current_winner = current_winner

    def print_board(self):
        print('''current state:
        | 1 | 2 | 3 |
        | 4 | 5 | 6 |
        | 7 | 8 | 9 |

        ''')
        print(f'''X,O state:
        | {self.cells[0]} | {self.cells[1]} | {self.cells[2]} |
        | {self.cells[3]} | {self.cells[4]} | {self.cells[5]} |
        | {self.cells[6]} | {self.cells[7]} | {self.cells[8]} |''')

    def available_moves(self):
        available_list_index = []
        coun = 0
        for iter in self.cells:
            if iter == ' ':
                available_list_index.append((coun))
            coun += 1

        return available_list_index

    def is_valid_move(self, position):
        position_index = int(position) - 1
        lis_index = self.available_moves()
        if position_index in lis_index:
            return True
        else:
            return False

    def make_move(self, position, symbol):
        if self.is_valid_move(position):
            self.cells[int(position) - 1] = symbol
            return True
        else:
            print("Not valid position please select other")
            return False

    def check_wins(self, symbol):
        if (self.cells[0] == self.cells[1] == self.cells[2] == symbol
                or
                self.cells[3] == self.cells[4] == self.cells[5] == symbol
                or
                self.cells[6] == self.cells[7] == self.cells[8] == symbol
                or
                self.cells[0] == self.cells[3] == self.cells[6] == symbol
                or
                self.cells[1] == self.cells[4] == self.cells[7] == symbol
                or
                self.cells[2] == self.cells[5] == self.cells[8] == symbol
                or
                self.cells[0] == self.cells[4] == self.cells[8] == symbol
                or
                self.cells[2] == self.cells[4] == self.cells[6] == symbol):
            return True
        else:
            return False

    def is_draw(self, symbol):
        temp_list = []
        if self.available_moves() == temp_list:
            if self.check_wins(symbol) == False:
                return True

        else:
            return False


from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, game_board):
        pass


class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game_board):
        move = input("Enter Position (1-9):\n")
        move = int(move)
        move_index = move - 1
        while not (0 <= move_index <= 8):
            print('Please enter position between (1-9):\n')
            move = input("Enter Position (1-9):\n")
            move = int(move)
            move_index = move - 1

        while not game_board.is_valid_move(str(move)):
            move = input("That position is already taken. Try again.")
            move = int(move)
            move_index = move - 1

        else:
            return move_index


import random


class ComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game_board):
        move = random.randint(1, 9)
        move_index = move - 1

        while not game_board.is_valid_move(str(move)):
            print("Invalid Position Computer Player will choose another")
            move = random.randint(1, 9)
            move_index = move - 1

        else:
            return move - 1  # index of movement in cells


class GameEngine:
    def __init__(self, players, current_player=0):
        self.players = players
        self.current_player = current_player
        cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.board = GameBoard(cells)
        self.players[0] = players[0]
        self.players[1] = players[1]
        self.players[0].symbol = 'X'
        self.players[1].symbol = 'O'

    def select_mode(self):
        mode = input('''
        Please select the mode you need:
        1 -->for Human vs Human 
        2 -->for Human vs Computer
        ''')
        if mode == '1':
            self.players[0] = HumanPlayer('X')
            self.players[1] = HumanPlayer('O')
        elif mode == '2':
            self.players[0] = HumanPlayer('X')
            self.players[1] = ComputerPlayer('O')

        else:
            print("Please select Valid mode")

    def switch_player(self):
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0
        else:
            pass

    def play(self):
        self.select_mode()
        win = 0
        draw = 0
        # print board
        self.board.print_board()

        while not (win or draw):
            # get index of move
            move = self.players[self.current_player].get_move(self.board)
            # if this index is valid write it inside board
            if self.board.make_move(str(move + 1), self.players[self.current_player].symbol):
                self.board.print_board()
                win = self.board.check_wins(self.players[self.current_player].symbol)
                draw = self.board.is_draw(self.players[self.current_player].symbol)
                if win:
                    print(f" Player {self.players[self.current_player].symbol} Wins")
                    break
                elif draw:
                    print(f"Game Draw")
                    break
                self.switch_player()


            else:
                pass
        else:
            if win:
                print(f" Player {self.players[self.current_player].symbol} Wins")
            elif draw:
                print(f"Game Draw")


cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board = GameBoard(cells)
player1 = HumanPlayer(board)
player2 = HumanPlayer(board)
players = [player1, player2]

game = GameEngine(players)
game.play()
