from board import Board
from player import Player
import time

class Game(object):
    """docstring for Game."""
    def __init__(self):
        print "Welcome to Jeopardy!"
        time.sleep(2)
        print "What is your name?"
        self.player = Player(raw_input())
        self.board = Board()
        self.board.display_whole_board()


Game()
