"""
test unitaires
"""
import unittest
from translator import english_to_french, french_to_english, norvegian_to_french, french_to_norvegian

class testTranslator(unittest.TestCase):
    def test_english_to_FrenchOK(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    
    def test_english_to_FrenchNOK(self):
        self.assertNotEqual(english_to_french('Bye'),'Bonjour')

    def test_french_to_englishOK(self):
        self.assertEqual(french_to_english('bonjour'),'Hello')
   
    def test_french_to_englishNOK(self):
        self.assertNotEqual(french_to_english('Au revoir'),'Hello')

    def test_norvegian_to_FrenchOK(self):
        self.assertEqual(norvegian_to_french('Tak'),'Merci')
    
    def test_norvegian_to_FrenchNOK(self):
        self.assertNotEqual(norvegian_to_french('öl'),'Merci')

    def test_french_to_norvegianOK(self):
        self.assertEqual(french_to_norvegian('Merci'),'Tak')
   
    def french_to_norvegianNOK(self):
        self.assertNotEqual(french_to_norvegian('Merci'),'Bière')
if __name__=='__main__':
    unittest.main()