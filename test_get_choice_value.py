import unittest

class TestGetChoiceValue(unittest.TestCase):
    def test_get_correct_value(self):
        for choice in CHOICES:
            self.assertEqual(get_choice_value(choice), VALUE_DICT[choice])

if __name__ == "__main__":
    unittest.main()