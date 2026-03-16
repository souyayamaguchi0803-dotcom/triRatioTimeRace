from random import randint

# 問題リスト
QUESTIONS = ["sin0°", "sin30°", "sin45°", "sin60°", "sin90°"]

# 問題を生成する関数
def generate_question():
    question_number = randint(0, 4)
    return QUESTIONS[question_number]