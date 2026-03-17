CHOICES = ["a", "b", "c", "d", "e"]

VALUE_DICT = {
	CHOICES[0] : "0",
    CHOICES[1] : "1/2",
    CHOICES[2] : "√2/2",
    CHOICES[3] : "√3/2",
    CHOICES[4] : "1"
}

def is_valid_choice(choice):
    return choice in CHOICES

def get_choice_value(choice):
    if not is_valid_choice(choice):
        raise ValueError("get_choice_value: invalid choice")
    return VALUE_DICT[choice]