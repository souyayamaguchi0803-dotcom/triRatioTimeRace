import unittest
from generate_question import generate_question, QUESTIONS

class TestGenerateQuestion(unittest.TestCase):
    def test_question_is_in_questions(self):
        self.assertTrue(generate_question() in QUESTIONS)
        
if __name__ == "__main__":
    unittest.main()