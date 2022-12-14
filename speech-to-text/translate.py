
from deep_translator import GoogleTranslator

def translate(file_name):
    # examples using google translate
    translator = GoogleTranslator(source="auto", target="spanish")

    # file translation
    result_file = translator.translate_file(file_name)
    translated_text = 'translated_text.txt'
    with open(translated_text, mode= 'w+', encoding='utf-8') as f:
            f.write(result_file + '\n')
    
    return translated_text
    # print("file translation: ", result_file)
