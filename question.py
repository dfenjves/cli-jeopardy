import requests
import json

class Question(object):
    """Jeopardy Question Class"""
    def __init__(self, question, answer, category, value):
        # q = requests.get('http://jservice.io/api/clues?category='+ str(category_id) +'&value='+ str(value))
        # question_data = q.json()
        self.question = question
        self.answer = answer
        self.category = category
        self.value = value
        self.unused = True

    def display(self):
        if self.unused:
            card ="     " + str(self.value) + "     |"
        else:
            card = "   " + " X " + "   |"
        return card

# q = Question(230,400)
# print q.category
# print q.question
#
# print q.display()
