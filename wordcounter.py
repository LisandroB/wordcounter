import unittest;

def wordCounter(phrase):
    return len(phrase.split())

class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(wordCounter("Hola, ¿cómo estás?"), 3)
    def test_simple(self):
        self.assertEqual(wordCounter("hola"), 1);
    def test_3(self):
        self.assertEqual(wordCounter("aaaaaaa aaaaaaaa"), 2)
    def test_4(self):
        self.assertEqual(wordCounter("Descansa en paz maestro... Siempre que te escuche, te recordaré con nostalgia."), 12)
        
if __name__ == '__main__':
    unittest.main();