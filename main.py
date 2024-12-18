from jsonToText import json_to_text_file
from translation_model import translate_file
from replace_texts import replace_json_texts

def main():
    # Ask for the input JSON file name
    json_file = input("Enter the path to the JSON file: ")

    # Generate file names
    text_output_file = "texts_for_translation.txt"
    translated_output_file = "translated_texts.txt"

    # Extract texts from the JSON
    json_to_text_file(json_file, text_output_file)

    # Ask for language inputs
    src_lang = input("Enter the source language (e.g., 'English'): ")
    tgt_lang = input("Enter the target language (e.g., 'Turkish'): ")

    try:
        # Translate the extracted texts
        translate_file(text_output_file, translated_output_file, src_lang, tgt_lang)
    except ValueError as e:
        print(e)
        return

    # Automatically name the final JSON file based on the target language
    output_json_file = f"{tgt_lang.title().replace(' ', '_')}.json"
    try:
        # Replace original JSON texts with translated texts
        replace_json_texts(json_file, translated_output_file, output_json_file)
    except Exception as e:
        print(f"An error occurred during JSON text replacement: {e}")
        return

    print(f"\nAll steps completed! Updated JSON saved at: {output_json_file}")

if __name__ == "__main__":
    main()

