from question import Question
import time
from fuzzywuzzy import fuzz

print "Welcome to Jeopardy!"
another_question = True

def serve_new_question():
    new_question = Question()
    print "The category is..." + new_question.category
    time.sleep(2)
    print "..."
    print new_question.question

    user_response = raw_input()
    fuzz_ratio = fuzz.ratio(new_question.answer.lower(), user_response.lower())

    if fuzz_ratio > 65:
        print "YOU ARE CORRECT - Fuzz ratio:" + str(fuzz_ratio) + new_question.answer
    else:
        print "Sorry, That's wrong. Fuzz ratio: " + str(fuzz_ratio)
        print "The correct answer was " + new_question.answer

while another_question == True:
    serve_new_question()
    if raw_input("Try another?") == "y":
        print "ok"
    else:
        print "goodbye"
        another_question = False

# to do:
# allow multiple questions
# board
# scoring
# timer
