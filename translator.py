from translate import Translator

def translate_function(input_str, from_lang, to_lang):
    translator = Translator(from_lang=from_lang,to_lang=to_lang)
    translation = translator.translate(input_str)
    return translation


def main():
    output = translate_function("This is a pen.", from_lang="en", to_lang='es')
    print(output)