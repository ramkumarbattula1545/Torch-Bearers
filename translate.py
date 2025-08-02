# # modules/translate.py
# from transformers import pipeline

# # Load translation pipelines
# translation_models = {
#     "Hindi": "Helsinki-NLP/opus-mt-en-hi",
#     "Telugu": "Helsinki-NLP/opus-mt-en-te",
#     "Spanish": "Helsinki-NLP/opus-mt-en-es",
#     "French": "Helsinki-NLP/opus-mt-en-fr"
# }

# def translate_text(text, target_lang="Hindi"):
#     """
#     Translate English text into selected language using Hugging Face models.
#     """
#     if target_lang == "English":
#         return text  # No translation needed

#     model_name = translation_models.get(target_lang)
#     if not model_name:
#         return text

#     translator = pipeline("translation", model=model_name)
#     result = translator(text, max_length=512)
#     return result[0]['translation_text']


from transformers import pipeline

# Map language to correct model
TRANSLATION_MODELS = {
   # Multi Indian languages (includes te)
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "French": "Helsinki-NLP/opus-mt-en-fr"
}

def translate_text(text, target_lang="Hindi"):
    """
    Translate text from English to selected language using Hugging Face models.
    """
    model_name = TRANSLATION_MODELS.get(target_lang)
    if not model_name:
        raise ValueError(f"Translation model for {target_lang} not available")

    # Initialize translation pipeline
    translator = pipeline("translation", model=model_name)

    # Perform translation
    translated = translator(text, max_length=512)[0]['translation_text']
    return translated
