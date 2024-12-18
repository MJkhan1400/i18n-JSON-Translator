from jsonToText import json_to_text_file
from translation_model import translate_file

def main():
    json_file = input("Enter the path to the JSON file: ")
    text_output_file = input("Enter the path to save the extracted texts (e.g., texts_for_translation.txt): ")

    json_to_text_file(json_file, text_output_file)

    translated_output_file = input("Enter the path to save the translated texts (e.g., translated_texts.txt): ")
    src_lang = input("Enter the source language (e.g., 'English'): ")
    tgt_lang = input("Enter the target language (e.g., 'Turkish'): ")

    try:
        translate_file(text_output_file, translated_output_file, src_lang, tgt_lang)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

