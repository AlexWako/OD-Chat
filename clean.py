import re

def clean(texts):
    r_tokens = []
    for text in texts:
        tokens = text.split()
    
        for t in tokens:
            r_tokens.append(re.sub(r'[^\w\s]', '', t).lower())
    
    return r_tokens

def tokenize_space(sentences):
    max_len = len(max(sentences, key = len))
    r_token = []
    for sentence in sentences:
        while len(sentence) < max_len:
            sentence.append(0)
        r_token.append(sentence)
    return r_token
    