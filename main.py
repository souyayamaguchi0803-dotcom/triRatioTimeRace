from generate_question import generate_question
from choices import show_choices

def main_game():
    question = generate_question()
    print(f"{question} = ?")
    
    choices = show_choices()
    print(choices)
    
    
if __name__ == "__main__":
    main_game()