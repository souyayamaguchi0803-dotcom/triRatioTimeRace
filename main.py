from generate_question import generate_question
from choices import show_choices

def main_game():
    # 問題を表示
    question = generate_question()
    print(f"{question} = ?")
    
    # 選択肢を表示
    choices = show_choices()
    print(choices)
    
    
if __name__ == "__main__":
    main_game()