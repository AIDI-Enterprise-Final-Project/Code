"""
    Preprocessing file for AIDI 2004 fianl Project
"""
import nltk
from nltk.corpus import stopwords
import re
import string

all_punctuations = string.punctuation + '‘’,:”][],'

nltk_words = set(nltk.corpus.words.words())

def preprocess(text):
    text = text.lower() # lowercase every document

    text = "".join(re.sub(r"http\S+", "", text, flags=re.IGNORECASE))   # remove URLs
    text = "".join(re.sub(r"[@[a-zA-Z]+:]*", "", text, flags=re.IGNORECASE)) # remove patterns like --> @warriorwoman:
    text = "".join(re.sub(r"[@[a-zA-Z]+_]*", "", text, flags=re.IGNORECASE)) # remove patterns like --> @warriorwoman_:
    text = "".join(re.sub(r"w/ @[a-zA_Z]*", "", text, flags=re.IGNORECASE)) # remove patterns like --> w/ @realDonaldTrump
    text = "".join(re.sub(r"[@[a-zA-Z\d]+:]*", "", text, flags=re.IGNORECASE)) # remove patterns like --> @warriorwoman91:
    text = "".join(re.sub(r"[@[a-zA-Z\d]+_]*", "", text, flags=re.IGNORECASE)) # remove patterns like --> @warriorwoman91_:
    text = "".join(re.sub(r"[0-9]*", "", text, flags = re.IGNORECASE))  # remove numbers
    text = "".join(re.sub('(\n|\r|\xa0)', "", text, flags = re.IGNORECASE))  # remove escape characters
    text = "".join(re.sub('(\[.\])', "", text, flags = re.IGNORECASE))  # remove patterns like [...]
    text = "".join(re.sub(r"[0-9]*", "", text, flags = re.IGNORECASE))  # remove numbers
    text = "".join(re.sub(r"( \w )*", "", text, flags = re.IGNORECASE)) # remove single characters
    
    
    no_punct = "".join([i for i in text if i not in all_punctuations])  # removing all punctuations
    
    words = no_punct.split()                   # splitting all the words
    no_stop_words = " ".join([i for i in words if i not in stopwords.words('english')])  # removing stop words
    
    lemmer = nltk.stem.WordNetLemmatizer()    # instanctiate the lemmatizer
    return " ".join([lemmer.lemmatize(word,'v') for word in no_stop_words.split()]) # lemmatize the words in the data

