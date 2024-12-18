import json

def extract_texts(data, result=None):
    """
    Recursively extracts all text values from a nested JSON structure.
    """
    if result is None:
        result = []

    if isinstance(data, dict):
        for key, value in data.items():
            extract_texts(value, result)
    elif isinstance(data, list):
        for item in data:
            extract_texts(item, result)
    elif isinstance(data, str):
        result.append(data)
    return result

def json_to_text_file(json_file_path, output_file_path):
    """
    Reads a JSON file, extracts all text values, and writes them to a text file.
    """
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    
    all_texts = extract_texts(json_data)
    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        for text in all_texts:
            out_file.write(text + '\n')  # Write each text to a new line

    print(f"Texts have been written to {output_file_path}")

