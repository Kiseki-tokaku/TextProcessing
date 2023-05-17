import nltk
import spacy

def sentence_segmentation(text, language="english", NLTK =False):
    sentences = []
    if NLTK:
        sentences = nltk.sent_tokenize(text)
    else:
        if language == "portuguese":
            nlp = spacy.load('pt_core_web_sm',disable=['tagger', 'ner','lemmatizer'])
        else:
            nlp = spacy.load('en_core_web_sm',disable=['tagger', 'ner','lemmatizer'])
            
        if len(text) >500000:
            ListOfChunks = chunks(text, 500000)
            for chunk in ListOfChunks:
                doc= nlp(chunk)
                
                for sentence in doc.sents:
                    sentences.append(sentence.text)
        else:
            doc= nlp(text)
            
            for sentence in doc.sents:
                sentences.append(sentence.text)
                
    return sentences

def chunks(text, n):
    ListOfChunks=[]
    
    for i in range(0, len(text), n):
        ListOfChunks.append(text[i:i+n])
    
    return ListOfChunks