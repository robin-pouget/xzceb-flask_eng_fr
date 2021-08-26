"""pour la traduction de mots en francais anglais et anglais francais"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

def get_language_translator(apikey, version, url):
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator)
    language_translator.set_service_url(url)
    return language_translator

def english_to_french(english_text):
    """ traduit anglais en francais"""
    
    if english_text is None:
        french_text = None
    else:
        l_t = get_language_translator(apikey, version, url)
        translation = l_t.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ traduit francais en anglais"""
    if french_text is None:
        english_text=None
    else:
        l_t = get_language_translator(apikey, version, url)
        translation = l_t.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text =  translation['translations'][0]['translation']
    return english_text
