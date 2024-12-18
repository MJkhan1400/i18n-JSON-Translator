from jsonToText import json_to_text_file
from translation_model import translate_file
from replace_texts import replace_json_texts

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
        return

    output_json_file = input("Enter the path to save the updated JSON file (e.g., Updated_Turkish.json): ")
    try:
        replace_json_texts(json_file, translated_output_file, output_json_file)
    except Exception as e:
        print(f"An error occurred during JSON text replacement: {e}")
        return

    print(f"\nAll steps completed! Updated JSON saved at: {output_json_file}")

if __name__ == "__main__":
    main()

