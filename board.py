from IPython import embed
import random
from category import Category

class Board(object):
    """docstring for Board. Accepts an array of question objects and displays in board format."""
    line =   "______________________________________________________________________\n"
    filler = "|             |             |             |             |             |\n"

    def __init__(self):
        self.categories = []
        for i in range(0,5):
            self.categories.append(Category(random.randint(1,1000)))

    #The functions below are for displaying the board:

    def display_row(self, val):
        row = self.line+ self.filler +"|"
        for category in self.categories:
            if str(val) in category.questions:
                row += category.questions[str(val)].display()
            else:
                row += "     " + " X " + "     |"
        row += "\n" + self.filler + self.line
        print row

    def display_all_question_rows(self):
        for val in [100,200,300,400,500]:
            self.display_row(val)

    def display_category_row(self):
        row = self.line+ self.filler +"|"
        for category in self.categories:
            row += category.display_square()
        row += "\n" + self.filler + self.line
        print row

    def display_whole_board(self):
        self.display_category_row()
        self.display_all_question_rows()



new_board = Board()
# new_board.display_all_question_rows()
new_board.display_whole_board()
