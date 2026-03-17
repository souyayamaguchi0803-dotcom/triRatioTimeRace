import unittest
from generate_question import generate_question, QUESTIONS

class TestGenerateQuestion(unittest.TestCase):
    def test_question_is_in_questions(self):
        for _ in range(100):
	        self.assertIn(generate_question(), QUESTIONS)
        
if __name__ == "__main__":
    unittest.main()