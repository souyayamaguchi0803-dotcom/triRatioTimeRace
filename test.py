import unittest
from sinValue import sinValue

class testSinValue(unittest.TestCase):
    def test_sin_0(self):
        self.assertEqual(sinValue("sin0°"), "0")
    def test_sin_30(self):
        self.assertEqual(sinValue("sin30°"), "1/2")
    def test_sin_45(self):
        self.assertEqual(sinValue("sin45°"), "√2/2")
    def test_sin_60(self):
        self.assertEqual(sinValue("sin60°"), "√3/2")
    def test_sin_90(self):
        self.assertEqual(sinValue("sin90°"), "1")
        
if __name__ == "__main__":
    unittest.main()