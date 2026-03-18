from generate_question import generate_question
from choices import show_choices, get_choice_value
from judge_answer import judge

def main_game():
    # 問題を表示
    question = generate_question()
    print(f"{question} = ?")
    
    # 選択肢を表示
    choices = show_choices()
    print(choices)
    
    # 回答を取得
    print("your answer > ", end="")
    answer = input()
    
    # 正誤判定
    answer_value = get_choice_value(answer)
    result = judge(question, answer_value)
    print(result)
    
    
if __name__ == "__main__":
    main_game()