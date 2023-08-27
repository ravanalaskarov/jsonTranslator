import os
import translators as ts
import json

translatorList: list = ts.translators_pool
for index, service in enumerate(translatorList):
    print(f"{index} - {service}")


serviceIndex = input("\nEnter the index of the translation service (Leave empty for Google Translate): ")

if serviceIndex.isnumeric():
    translator = translatorList[serviceIndex]
else:
    translator = 'google'

print('''
      

Supported Languages can be found at:
      
https://github.com/UlionTse/translators#supported-languages (Use Language of Translator for keys)
      
      
''')

from_language = input("Enter the source language (Leave empty for auto recognition): ") or 'auto'

to_language = input("Enter the translate language (Leave empty for English): ") or 'en'

json_source_location = input("Enter the complete path of the json file (Like: C:\\Users\\Admin\\translation.json): ")

with open(json_source_location, 'r', encoding='utf-8') as openfile:
    json_source_object = json.load(openfile)

translated_json_data = {}

jsonLen = len(json_source_object)
for index, key in enumerate(json_source_object):
    value = json_source_object[key]
    translated_string = ts.translate_text(value, translator = translator, from_language = from_language, to_language = to_language)
    translated_json_data[key] = translated_string
    print(f'{index + 1}/{jsonLen}', end='\r')

file_name = str(f"{to_language}.json")

with open(file_name, "w", encoding='utf-8') as outfile:
    json.dump(translated_json_data, outfile, ensure_ascii=False, indent=4)

print(f"\n\nTranslated file path:\n{os.path.abspath(outfile.name)}\n")
