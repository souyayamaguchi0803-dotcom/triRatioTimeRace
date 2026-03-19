from generate_question import generate_question
from choices import CHOICES, show_choices, is_valid_choice, get_choice_value
from judge_answer import judge

current_score = 0

def main_game():
    print()
    
    # 問題を表示
    question = generate_question()
    print(f"{question} = ?")
    
    # 選択肢を表示
    choices = show_choices()
    print(choices)
    print()
    
    # 回答を取得
    print("your answer > ", end="")
    answer = input()
    
    # 正誤判定
    if is_valid_choice(answer):
        answer_value = get_choice_value(answer)
        result = judge(question, answer_value)
        print(result)
        
        # 正解時は得点増加
        if result == "Correct!":
            current_score += 1
    else:
        print(f"please choice answer from {CHOICES[0]} ~ {CHOICES[-1]}.")
    
    print()
    
    
if __name__ == "__main__":
    main_game()