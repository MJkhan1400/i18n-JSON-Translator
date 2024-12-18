import json

def replace_texts_in_json(data, translated_lines, index=0):
    """
    Recursively replaces text values in the JSON structure with translated texts.

    Args:
        data: The JSON object (can be dict, list, or str).
        translated_lines: List of translated text lines.
        index: Current index in the translated lines.

    Returns:
        Updated JSON object with replaced texts and the next index.
    """
    if isinstance(data, dict):
        for key in data:
            data[key], index = replace_texts_in_json(data[key], translated_lines, index)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i], index = replace_texts_in_json(data[i], translated_lines, index)
    elif isinstance(data, str):
        # Replace string with the next translated line
        if index < len(translated_lines):
            return translated_lines[index], index + 1
    return data, index

def replace_json_texts(original_json_file, translated_text_file, output_json_file):
    """
    Reads the original JSON file and translated texts, replaces texts, and writes to a new JSON file.

    Args:
        original_json_file: Path to the original JSON file.
        translated_text_file: Path to the file containing translated texts.
        output_json_file: Path to save the updated JSON file.
    """
    # Load the original JSON file
    with open(original_json_file, 'r', encoding='utf-8') as infile:
        original_data = json.load(infile)

    # Read the translated text lines
    with open(translated_text_file, 'r', encoding='utf-8') as transfile:
        translated_lines = [line.strip() for line in transfile if line.strip()]

    # Replace texts in the JSON
    updated_data, _ = replace_texts_in_json(original_data, translated_lines)

    # Save the updated JSON to the output file
    with open(output_json_file, 'w', encoding='utf-8') as outfile:
        json.dump(updated_data, outfile, indent=4, ensure_ascii=False)

    print(f"Updated JSON has been saved to {output_json_file}")

