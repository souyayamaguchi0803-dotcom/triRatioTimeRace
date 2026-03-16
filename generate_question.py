from random import randint

QUESTIONS = ["sin0°", "sin30°", "sin45°", "sin60°", "sin90°"]

def generate_question():
    question_number = randint(0, 4)
    return QUESTIONS[question_number]