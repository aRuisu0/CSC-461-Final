
from deep_translator import GoogleTranslator

# examples using google translate
translator = GoogleTranslator(source="auto", target="spanish")

# file translation
result_file = translator.translate_file("test.txt")
print("file translation: ", result_file)
