
from deep_translator import GoogleTranslator

def translate():
    # examples using google translate
    translator = GoogleTranslator(source="auto", target="english")

    # file translation
    file_name = input('Enter name of file to translate (File must be in same directory): ')
    result_file = translator.translate_file(file_name)
    print("file translation: ", result_file)
