from board import Board
from player import Player
import time
from fuzzywuzzy import fuzz

class Game(object):
    """docstring for Game."""
    def __init__(self):
        print "Welcome to Jeopardy!"
        time.sleep(1)
        print "What is your name?"
        self.player = Player(raw_input())
        print "Hello " + self.player.name + ", get ready to play!"
        self.board = Board()
        while self.finished_board() == False:
            self.board.display_whole_board()
            self.prompt_and_play()


    def prompt_and_play(self): #NEEDS WORK
        print "Please select a category from the board"
        selected_category = raw_input()
        print "Please select a value from that category"
        selected_value = raw_input()
        for cat in self.board.categories:
            fuzz_ratio = fuzz.ratio(cat.title, selected_category)
            if cat.title == selected_category:
                self.player.score += cat.questions[selected_value].ask()
        print self.player.name+", your score is now $" + str(self.player.score)

    def finished_board(self):
        for cat in self.board.categories:
            for val in [100,200,300,400,500]:
                if cat.questions[str(val)].unused == True:
                    return False
        return True
Game()
