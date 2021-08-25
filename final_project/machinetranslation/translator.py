"""pour la traduction de mots en francais anglais et anglais francais"""

import os
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

def english_to_french(english_text, l_t):
    """ traduit anglais en francais"""

    translation = l_t.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text,l_t):
    """ traduit francais en anglais"""
    translation = l_t.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text =  translation['translations'][0]['translation']
    return english_text
