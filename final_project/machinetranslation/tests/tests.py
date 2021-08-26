

import os
import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator)
language_translator.set_service_url(url)

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