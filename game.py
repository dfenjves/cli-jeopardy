from board import Board
from player import Player
import time
from fuzzywuzzy import fuzz

class Game(object):
    """docstring for Game."""
    def __init__(self):
        print "Welcome to Jeopardy!"
        time.sleep(2)
        print "What is your name?"
        self.player = Player(raw_input())
        print "Hello " + self.player.name + ", get ready to play!"
        self.board = Board()
        self.board.display_whole_board()
        self.prompt_and_play()
        self.board.display_whole_board()
        self.prompt_and_play()
        self.board.display_whole_board()
        self.prompt_and_play()
        self.board.display_whole_board()

    def prompt_and_play(self): #NEEDS WORK
        print "Please select a category from the board"
        selected_category = raw_input()
        print "Please select a value from that category"
        selected_value = raw_input()
        for cat in self.board.categories:
            fuzz_ratio = fuzz.ratio(cat.title, selected_category)
            if fuzz_ratio > 0.75:
                self.player.score += cat.questions[selected_value].ask()
            else:
                print "Unable to find that Category"


Game()
