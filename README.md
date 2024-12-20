# i18n JSON Translator

i18n JSON Translator is a powerful, developer-focused tool designed to streamline the process of localizing your website or app. It allows you to effortlessly (but not yet accurately) translate your i18n-related JSON files into any language, setting you up for globalizing your websites and apps.

This program leverages the Hugging Face `transformers` library and the `facebook/m2m100_1.2B` multilingual model to extract, translate, and update JSON files containing text data. While the translations are not perfect and may require manual adjustments, this tool provides a fast and efficient way to kickstart the localization process.

## Features

- **JSON Text Extraction**: Automatically extracts all text values from a nested JSON structure.
- **Multilingual Translation**: Translates extracted texts into any language using a pretrained multilingual model.
- **JSON Text Replacement**: Replaces the original JSON's text values with their translated equivalents.
- **Fully Localizable**: Supports offline use for privacy-conscious users.


## Recommended Setup
I recommend using a Conda environment with Python 3.10.12 to ensure compatibility. Follow these steps to set up the environment:

1. Create a new Conda environment:
   ```bash
   conda create -n i18n_translator python=3.10.12 -y
   ```
2. Activate the environment:
   ```bash
   conda activate i18n_translator
   ```
3. Install cudnn if you dont have:
	 ```bash
	 conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
	 ```
4. Install dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

---

## Input and Output Example

### Input
- **JSON File**: A file containing nested or flat text values for localization.
  Example: `English.json`
  ```json
  {
    "orderBy": "Order by",
    "paymentSuccess": "Payment Success",
    "shoppingBookingStatus": {
      "billDetails": "Bill Details"
    }
  }
  ```

- **Languages**: Source language (e.g., `English`) and target language (e.g., `Turkish`).

### Output
- **Translated JSON**: Automatically generated file named after the target language (e.g., `Turkish.json`):
  ```json
  {
    "orderBy": "Sipariş Ver",
    "paymentSuccess": "Ödeme Başarılı",
    "shoppingBookingStatus": {
      "billDetails": "Fatura Detayları"
    }
  }
  ```

---

## Process Overview

1. **Text Extraction**: Extracts all text values from the input JSON file into a text file named `texts_for_translation.txt`.
2. **Translation**: Translates the extracted texts and saves the output in `translated_texts.txt`.
3. **JSON Update**: Replaces the original JSON's text values with the translated texts and outputs the final JSON file (e.g., `Turkish.json`).

---

## Advantages

- **Developer-Friendly**: Simple input-output workflow tailored for developers.
- **Kickstart Localization**: Provides a starting point for translating JSON files into multiple languages.
- **Multilingual Model**: Supports a wide range of languages.

---

## Disadvantages

- **Translation Accuracy**: The pretrained model may not produce accurate translations for all text values.
- **Manual Adjustments Required**: Developers should review and refine translations before using them in production.

---

## Caution

### Offline Usage
You can run this program without an internet connection if the model and tokenizer are downloaded first. Once downloaded, all operations are performed locally, ensuring your data stays private.

### Privacy Caution
If you handle sensitive data and want to ensure privacy:
1. **Run the program offline**: Disconnect from the internet after the model download is complete.
2. **Clear the Hugging Face cache** after completing your translations:
   ```bash
   rm -rf ~/.cache/huggingface
   ```

This ensures that no data remains on your local machine related to the translation process.