import unittest
from judge_answer import judge

class TestJudgeAnswer(unittest.TestCase):
    def test_correct_answer(self):
        params = [
			("sin0°", "0"),
            ("sin30°", "1/2")
		]
        for question, answer in params:
            with self.subTest(question=question, answer=answer):
                self.assertEqual(judge(question, answer), "Correct!")
    def test_wrong_answer(self):
        params = [
			("sin0°", "1"),
            ("sin30°", "1")
		]
        for question, answer in params:
            with self.subTest(question=question, answer=answer):
                self.assertEqual(judge(question, answer), "Oops!")

if __name__ == "__main__":
    unittest.main()