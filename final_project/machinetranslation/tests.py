"""
test unitaires
"""
import unittest
from translator import english_to_french, french_to_english

class testTranslator(unittest.TestCase):
    def test_english_to_French(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('bonjour'),'Hello')

    def test_null_to_French(self):
        self.assertEqual(english_to_french(None),None)
    
    def test_null_to_english(self):
        self.assertEqual(french_to_english(None),None)


if __name__=='__main__':
    unittest.main()