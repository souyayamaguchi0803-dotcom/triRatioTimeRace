import time
from generate_question import generate_question
from choices import CHOICES, show_choices, is_valid_choice, get_choice_value
from judge_answer import judge

def main_game():
    question_num = 0
    current_score = 0
    target_score = 5
    
    start_time = time.perf_counter()

    while current_score < target_score:
        question_num += 1
        
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
    
    # 結果発表
    print("=== result ===")
    
    # 正答率表示
    print(f"accuracy: {current_score}/{question_num}")
    
    # クリアタイム表示
    end_time = time.perf_counter()
    clear_time = end_time - start_time
    print(f"time: {clear_time:.2f}")
    
    print()
    
    
if __name__ == "__main__":
    main_game()