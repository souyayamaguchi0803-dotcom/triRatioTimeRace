import unittest
from choices import show_choices, CHOICES, VALUE_DICT

class TestShowChoices(unittest.TestCase):
    def test_show_chioces(self):
        choices_list = show_choices()
        for choice in CHOICES:
            self.assertIn(f"{choice}. {VALUE_DICT[choice]}", choices_list)

if __name__ == "__main__":
    unittest.main()