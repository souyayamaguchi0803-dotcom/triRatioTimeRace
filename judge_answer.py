from sin_value import sin_value

def judge(question, answer):
    if answer == sin_value(question): # 正解の場合
        return "Correct!"
    else: # 不正解の場合
        return "Oops!"