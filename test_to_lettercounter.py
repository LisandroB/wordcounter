import unittest
from lettercounter import letterCounter 

class testCase(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(letterCounter("catorce"), 7)
    def test_dos(self):
        self.assertEqual(letterCounter("uno"), 3)
    def test_tres(self):
        self.assertEqual(letterCounter("cuarenta y cinco"), 14)
    def test_cuatro(self):
        self.assertEqual(letterCounter("albóndiga esponjosa"), 18);
    def test_cinco(self):
        self.assertEqual(letterCounter("otor rino laringó logo"), 19)
if __name__ == '__main__':
    unittest.main();