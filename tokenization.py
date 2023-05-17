import spacy

def nlpexe(text,nlp,result):
    doc = nlp.make_doc(text)
    for token in doc:
        result.append(token.text)
    return result

def tokenization(text,language = "english"):
    
    result = []
    
    if language == 'portuguese':
        nlp = spacy.load('pt_core_news_sm',disable=['tagger', 'parser', 'ner'])
    elif language != "english":
        return "Wanted language is not avaiable"
    else:
        nlp = spacy.load('en_core_web_sm',disable=['tagger', 'parser', 'ner'])
    
    if len(text) >= 1000000:
        textWords = text.split()
        count = 0
        sentence = ""
        for word in textWords:
            if count+len(word)+1 < 1000000:
                sentence += word + " "
            else:
                result = nlpexe(sentence,nlp,result)
                count = 0
                sentence = ""
        if sentence != "":
            result = nlpexe(sentence,nlp,result)
    else:
        result = nlpexe(text,nlp,result)
    return result