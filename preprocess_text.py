import jaconv
import unicodedata
import neologdn
import regex

def preprocess(text):

    # Neologd Normalization
    text = neologdn.normalize(text)

    # Normalization Form Compatibility Composition (NFKC)
    text = unicodedata.normalize("NFKC", text)

    # full-width characterization
    text = regex.sub(r'(\d)([,])(\d+)', r'\1\3', text)
    text = text.replace(",", "、")
    text = text.replace("，", "、")
    text = (jaconv.h2z(text, kana=True, digit=True, ascii=True))

    # remove zenkaku space
    text = text.replace("\u3000", "")

    return text
