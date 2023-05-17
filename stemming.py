import nltk

def stemming(text, language='english'):
    stem = nltk.stem.SnowballStemmer(language)
    text = ' '.join([stem.stem(word) for word in nltk.word_tokenize(text)])
    return text