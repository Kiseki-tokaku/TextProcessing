import re
from nltk.corpus import stopwords as s_words

def stopwords_removal(text, lang = "english"):
    text = re.sub(r"\W"," ",text)
    t_split = text.split()
    stopWords = s_words.words(lang)
    for word in t_split:
        if word.lower() in stopWords:
            t_split.pop(t_split.index(word))
    return t_split