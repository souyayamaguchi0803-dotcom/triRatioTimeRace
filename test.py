import unittest
from sinValue import sinValue

class testSinValue(unittest.TestCase):
    def test_sin_0(self):
        self.assertEqual(sinValue("sin0°"), "0")
        
if __name__ == "__main__":
    unittest.main()