import textwrap
import math
import random
import requests
import json
from question import Question

class Category(object):
    """docstring for Category."""
    def __init__(self, category_id):
        c = requests.get('http://jservice.io/api/category?id='+ str(category_id))
        category_data = c.json()
        self.questions = {} #populate this dictionary with the category's values:questions
        self.title = category_data['title'] #Category title
        #loop through the category and create new questions for each one.
        clues = category_data['clues'] #Get the clue data
        for c in clues:
            new_question = Question(c['question'], c['answer'], self.title, c['value'])
            if str(new_question.value) not in self.questions and new_question.value:
                self.questions[str(new_question.value)] = new_question

    def display_square_lines(self):
        box_width = 13
        # if len(self.title) <= 13:
        display = "{0: ^13}".format(self.title)+"|"
            # lines = [display, "              |"]
        # else:
            #split around the middle and place
            # display = textwrap.wrap(self.title, box_width)
            # lines = [display, "              |"]
        return display

def center_string(text, width): #takes in text and total width of string and centers in that string
    to_format ="{0: ^"+str(width)+"}"
    centered_string = to_format.format(text)


new_category = Category(random.randint(1,1000))
print new_category.display_square_lines()
