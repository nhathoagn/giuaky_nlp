import re

import nltk
from nltk import word_tokenize
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from pyvi import ViUtils
from spellchecker import SpellChecker
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
def Read_file():
    text = open('giuaky_nlp');
    raw = text.read();
    # print("Noi dung don text \n" , raw);
    return raw;
def tokenzie():
    raw = Read_file()
    tokens = word_tokenize(raw)
    # print("Tách các từ và hiển thị")
    # print(tokens)
    return tokens
def spellchecker():
    token = tokenzie()
    spell = SpellChecker()
    misspelled = spell.unknown(token)

    print("Tu co the  chinh ta:\n", str(misspelled))
    for word in misspelled:
        # Get the one `most likely` answer
        print(spell.correction(word))



def sent_tokenize():
    raw = Read_file()
    token = nltk.sent_tokenize(raw)
    print("tach cau\n" , token)
    return token
def stop_words():
   tokens= tokenzie()
   stop_words = set(stopwords.words('english'))
   filtered_sentence = []
   for w in tokens:
     if w not in stop_words:
         filtered_sentence.append(w)
   print("Thực hiện stop-word: \n", str(filtered_sentence))

def vocabulary():
    raw = Read_file()
    li = list(raw.split(" "))
    processed_docs = [doc.lower().replace(".","") for doc in li ]

    vocab = {}
    count = 0
    for doc in processed_docs:
        for word in doc.split():
            if word not in vocab:
                count = count + 1
                vocab[word] = count
    print("Bộ từ vựng:\n",vocab)
    return vocab;
def Stemming_Lemmatization():
    tokens = tokenzie()
    lancaster = LancasterStemmer()
    print("Thực hiện Stemming + Lemmatization")
    wordnet_lemmatizer = WordNetLemmatizer()
    print("{0:20}{1:20}{2:20}".format("Word","Stem","Lemma"))
    for word in tokens:
     print ("{0:20}{1:20}{2:20}".format(word,lancaster.stem(word),wordnet_lemmatizer.lemmatize(word, pos="v")))
def pos_tag():
    tokens = tokenzie()
    print(nltk.pos_tag(tokens))
def lowercasting():
   raw = Read_file()
   lowercasting = raw.lower()
   print("Chuyển về kiểu chữ thường:\n ", lowercasting)

def remove_special_characters():
    raw = Read_file()
    pattern = r'[^A-Za-z0-9]+'
    sample_tr = re.sub(pattern, " ", raw)
    print(sample_tr)
def remove_accents():
    print(ViUtils.remove_accents("Nguyễn Nhật Hoàng"));


if __name__ == '__main__':
    Read_file()
    tokenzie()
    spellchecker()

    # sent_tokenize()
    # stop_words()
    # vocabulary()
    # Stemming_Lemmatization()
    # pos_tag()
    # lowercasting()
    # remove_special_characters()
    # remove_accents()