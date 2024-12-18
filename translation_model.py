import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Language mapping
LANGUAGE_CODES = {
    "Afrikaans": "af", "Amharic": "am", "Arabic": "ar", "Asturian": "ast", "Azerbaijani": "az", "Bashkir": "ba",
    "Belarusian": "be", "Bulgarian": "bg", "Bengali": "bn", "Breton": "br", "Bosnian": "bs", "Catalan": "ca",
    "Cebuano": "ceb", "Czech": "cs", "Welsh": "cy", "Danish": "da", "German": "de", "Greeek": "el", "English": "en",
    "Spanish": "es", "Estonian": "et", "Persian": "fa", "Fulah": "ff", "Finnish": "fi", "French": "fr",
    "WesternFrisian": "fy", "Irish": "ga", "Gaelic": "gd", "Galician": "gl", "Gujarati": "gu", "Hausa": "ha",
    "Hebrew": "he", "Hindi": "hi", "Croatian": "hr", "Haitian": "ht", "Hungarian": "hu", "Armenian": "hy",
    "Indonesian": "id", "Igbo": "ig", "Iloko": "ilo", "Icelandic": "is", "Italian": "it", "Japanese": "ja",
    "Javanese": "jv", "Georgian": "ka", "Kazakh": "kk", "CentralKhmer": "km", "Kannada": "kn", "Korean": "ko",
    "Luxembourgish": "lb", "Ganda": "lg", "Lingala": "ln", "Lao": "lo", "Lithuanian": "lt", "Latvian": "lv",
    "Malagasy": "mg", "Macedonian": "mk", "Malayalam": "ml", "Mongolian": "mn", "Marathi": "mr", "Malay": "ms",
    "Burmese": "my", "Nepali": "ne", "Dutch": "nl", "Norwegian": "no", "NorthernSotho": "ns", "Occitan": "oc",
    "Oriya": "or", "Panjabi": "pa", "Polish": "pl", "Pushto": "ps", "Portuguese": "pt", "Romanian": "ro",
    "Russian": "ru", "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so",
    "Albanian": "sq", "Serbian": "sr", "Swati": "ss", "Sundanese": "su", "Swedish": "sv", "Swahili": "sw",
    "Tamil": "ta", "Thai": "th", "Tagalog": "tl", "Tswana": "tn", "Turkish": "tr", "Ukrainian": "uk", "Urdu": "ur",
    "Uzbek": "uz", "Vietnamese": "vi", "Wolof": "wo", "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo",
    "Chinese": "zh", "Zulu": "zu"
}

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("facebook/m2m100_1.2B")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/m2m100_1.2B")
print("Model and tokenizer loaded successfully.")

def get_language_code(language_name):
    """
    Converts a language name to its corresponding code.
    """
    return LANGUAGE_CODES.get(language_name.title(), None)

def translate_text(text, src_lang_code, tgt_lang_code):
    """
    Translates a given text from the source language to the target language.
    """
    tokenizer.src_lang = src_lang_code
    encoded_text = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_text, forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang_code])
    return tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

def translate_file(input_file, output_file, src_lang, tgt_lang):
    """
    Translates each line in the input file and writes the translated text to the output file.
    """
    src_lang_code = get_language_code(src_lang)
    tgt_lang_code = get_language_code(tgt_lang)

    if not src_lang_code or not tgt_lang_code:
        raise ValueError("Invalid source or target language name. Please check the list of supported languages.")

    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            line = line.strip()
            if line:
                translated_text = translate_text(line, src_lang_code, tgt_lang_code)
                outfile.write(translated_text + '\n')
                print(f"Original: {line} | Translated: {translated_text}")

    print(f"\nAll lines have been translated and saved to {output_file}")

