import translator
import unittest

class TestStringMethods(unittest.TestCase):

    def test_englist_to_french(self):
        self.assertTrue("bonjour", translator.english_to_french("hello"))

    def test_french_to_english(self):
        self.assertTrue("hello", translator.french_to_english("bonjour"))

if __name__ == '__main__':
    unittest.main()
