#pip install translate
from translate import Translator

translator = Translator(from_lang='English', to_lang='Spanish')
sentence = input("Enter the text to be translated: ")
result = translator.translate(sentence)
print(result)