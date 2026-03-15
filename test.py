import unittest
from sinValue import sin_value

class TestSinValue(unittest.TestCase):
    def test_sin_0(self):
        self.assertEqual(sin_value("sin0°"), "0")
    def test_sin_30(self):
        self.assertEqual(sin_value("sin30°"), "1/2")
    def test_sin_45(self):
        self.assertEqual(sin_value("sin45°"), "√2/2")
    def test_sin_60(self):
        self.assertEqual(sin_value("sin60°"), "√3/2")
    def test_sin_90(self):
        self.assertEqual(sin_value("sin90°"), "1")
        
if __name__ == "__main__":
    unittest.main()