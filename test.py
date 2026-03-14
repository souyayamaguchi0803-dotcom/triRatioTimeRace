import unittest

class testSinValue(unittest.TestCase):
    def sin0(self):
        self.assertEqual(sinValue("sin0°"), "0")
        
if __name__ == "__main__":
    unittest.main()