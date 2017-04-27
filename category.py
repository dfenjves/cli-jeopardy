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

    def display_square(self):
        lines = ["","",""]
        title_length = len(self.title)
        if title_length <= 13:
            display = "{0: ^13}".format(self.title)+"|"
            lines = ["             |", display, "              |"]
        else:
            display = "FIX FIX FIX"
            lines = ["             |", display, "              |"]
        return lines[1]



new_category = Category(random.randint(1,1000))
print new_category.display_square()
