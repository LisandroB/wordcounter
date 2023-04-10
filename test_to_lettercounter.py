import unittest
from lettercounter import letterCounter 

class testCase(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(letterCounter("catorce"), {'c': 2, 'a': 1, 't': 1, 'o': 1, 'r': 1, 'e': 1})
    def test_dos(self):
        self.assertEqual(letterCounter("unouno"), {'u': 2, 'n': 2, 'o': 2})
    def test_tres(self):
        self.assertEqual(letterCounter("a"), {"a": 1})
    def test_cuatro(self):
        self.assertEqual(letterCounter("hola"), {'h': 1, 'o': 1, 'l': 1, 'a': 1});
        
if __name__ == '__main__':
    unittest.main();