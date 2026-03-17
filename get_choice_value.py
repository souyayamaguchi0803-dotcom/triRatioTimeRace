CHOICES = ["a", "b", "c", "d", "e"]

VALUE_DICT = {
	CHOICES[0] : "0",
    CHOICES[1] : "1/2",
    CHOICES[2] : "√2/2",
    CHOICES[3] : "√3/2",
    CHOICES[4] : "1"
}

def get_choice_value(choice):
    return VALUE_DICT[choice]