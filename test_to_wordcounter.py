import unittest
from wordcounter import wordCounter;

class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(wordCounter("hola como estas hola"), {'hola': 2, 'como': 1, 'estas': 1})
    def test_simple(self):
        self.assertEqual(wordCounter("hola"), {'hola': 1});
    def test_3(self):
        self.assertEqual(wordCounter("aaaaaaa aaaaaaaa"), {'aaaaaaa': 1, 'aaaaaaaa': 1})

        
if __name__ == '__main__':
    unittest.main();