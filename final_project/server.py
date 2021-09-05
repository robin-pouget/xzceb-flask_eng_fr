from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", static_folder='static',template_folder='templates')
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.config['DEBUG'] = True

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.english_to_french(textToTranslate)
    if french_text is not None:
        return french_text
    else:
        return ""

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.french_to_english(textToTranslate)
    if english_text is not None:
        return english_text
    else:
        return ""

@app.route("/norvegianToEnglish")
def norvegianToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.norvegian_to_english(textToTranslate)
    if english_text is not None:
        return english_text
    else:
        return ""


@app.route("/englishToNorvegian")
def englishToNorvegian():
    textToTranslate = request.args.get('textToTranslate')    
    norvegian_text = translator.english_to_norvegian(textToTranslate)
    if norvegian_text is not None:
        return norvegian_text
    else:
        return ""
    

@app.route("/")
def renderIndexPage():    
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
