import unittest
from wordcounter import wordCounter;

class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(wordCounter("Hola, ¿cómo estás?"), 3)
    def test_simple(self):
        self.assertEqual(wordCounter("hola"), 1);
    def test_3(self):
        self.assertEqual(wordCounter("aaaaaaa aaaaaaaa"), 2)
    def test_4(self):
        self.assertEqual(wordCounter("Descansa en paz maestro... Siempre que te escuche, te recordaré con nostalgia."), 12)
    def test_5(self):
        self.assertEqual(wordCounter(" Those chaotic screams perfectly embody how much I sometimes want to pull my hair out on the worst of days.  This song is cathartic."), 24);
        
if __name__ == '__main__':
    unittest.main();