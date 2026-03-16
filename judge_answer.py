from sin_value import sin_value

def judge(question, answer):
    if answer == sin_value(question):
        return "Correct!"
    else:
        return "Oops!"