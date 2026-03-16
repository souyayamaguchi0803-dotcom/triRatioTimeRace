import unittest
from judge_answer import judge

class TestJudgeAnswer(unittest.TestCase):
    def test_correct_answer(self):
        self.assertEqual(judge("sin0°", "0"), "Correct!")

if __name__ == "__main__":
    unittest.main()