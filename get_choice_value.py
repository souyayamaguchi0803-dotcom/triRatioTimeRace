CHOICES = ["a", "b", "c", "d", "e"]

VALUE_DICT = {
	"a" : "0",
    "b" : "1/2",
    "c" : "√2/2",
    "d" : "√3/2",
    "e" : "1"
}

def get_choice_value(choice):
    return VALUE_DICT[choice]