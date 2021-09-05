"""
test unitaires
"""
import unittest
from translator import english_to_french, french_to_english, norvegian_to_english, english_to_norvegian

class testTranslator(unittest.TestCase):
    def test_english_to_FrenchOK(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    
    def test_english_to_FrenchNOK(self):
        self.assertNotEqual(english_to_french('Bye'),'Bonjour')

    def test_french_to_englishOK(self):
        self.assertEqual(french_to_english('bonjour'),'Hello')
   
    def test_french_to_englishNOK(self):
        self.assertNotEqual(french_to_english('Au revoir'),'Hello')

    def test_norvegian_to_englishOK(self):
        self.assertEqual(norvegian_to_english('Takk'),'Thanks')
    
    def test_norvegian_to_englishNOK(self):
        self.assertNotEqual(norvegian_to_english('ØI'),'Hello')

    def test_english_to_norvegianOK(self):
        self.assertEqual(english_to_norvegian('Beer'),'ØI')
   
    def test_english_to_norvegianNOK(self):
        self.assertNotEqual(english_to_norvegian('Beer'),'Tak')

if __name__=='__main__':
    unittest.main()