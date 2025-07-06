from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return f"Translation ({target_lang}):\n{translated}"
    except Exception as e:
        return f"Translation failed:\n{str(e)}"
