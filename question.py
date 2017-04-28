import requests
import json
import time
from fuzzywuzzy import fuzz

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
            card = "     " + " X " + "     |"
        return card

    def ask(self):
        print "For $"+ str(self.value) + " in the category '" + self.category +"'"
        time.sleep(1)
        print "..."
        print self.question

        user_response = raw_input()
        fuzz_ratio = fuzz.ratio(self.answer.lower(), user_response.lower())

        if fuzz_ratio > 65:
            print "YOU ARE CORRECT - The answer was:" + self.answer
            self.unused = False
            return self.value
        else:
            print "Sorry, That's wrong. "
            print "The correct answer was " + self.answer
            self.unused = False
            return (-1)*self.value

# q = Question("How am I?","Good", "Danny", 300)
# q.ask()
