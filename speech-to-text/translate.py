
from deep_translator import GoogleTranslator
import os

def translate(file_name):
    # examples using google translate
    translator = GoogleTranslator(source="auto", target="spanish")

    # file translation
    text_file = os.path.join("transcripts", file_name)
    result_file = translator.translate_file(text_file)
    translated_name = file_name + '_translated.txt'
#     translated_name = input('Enter name for new translated text: ') + '.txt'

    input_file = os.path.join("translated_transcripts", translated_name)
    with open(input_file, mode= 'w+', encoding='utf-8') as f:
            f.write(result_file + '\n')
    
    return translated_name
