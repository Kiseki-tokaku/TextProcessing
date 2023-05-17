import spacy

def lemmatization(text,language='english'):
    
    if language == 'english':
        nlp = spacy.load('en_core_web_sm',disable=['tagger', 'parser', 'ner'])
    elif language == 'portuguese':
        nlp = spacy.load('pt_core_news_sm',disable=['tagger', 'parser', 'ner'])

    if len(text) > 500000:
        ListOfChunks = chunks(text,500000)
        for chunk in ListOfChunks:
            doc = nlp(chunk)
            text = ' '.join([word.lemma_ for word in doc])
    else:
        doc = nlp(text)
        text = ' '.join([word.lemma_ for word in doc])
    
    return text

def chunks(text, n):
    ListOfChunks = []
    
    """successive n-sized chunks from l."""
    for i in range(0, len(text), n):
        ListOfChunks.append(text[i:i + n])
    
    return ListOfChunks