# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import nltk
from pyvi import ViTokenizer, ViPosTagger
from pyvi import ViUtils

from nltk.tokenize import sent_tokenize, word_tokenize
import re
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
nltk.download('averaged_perceptron_tagger')
def Read_file():
    text = open('giuaky_nlp');
    raw = text.read();
    print("Noi dung don text \n" + raw);
    return raw;
def sent_tokenize():
    raw = Read_file()
    txt = []
    for text in nltk.sent_tokenize(raw):
        txt.append(text)
    print("tach cau\n" , txt)
    return txt
def tokenzie():
    raw = Read_file()
    tokens = word_tokenize(raw)
    print("Tách các từ và hiển thị")
    print(tokens)
    return tokens
def remove_special_characters():
    raw = Read_file()
    pattern = r'[^A-Za-z0-9]+'
    sample_tr = re.sub(pattern, " ", raw)
    print(sample_tr)
    return sample_tr
def one_hot():
    sample_tr = remove_special_characters()
    raw = Read_file()
    data = sample_tr

    print("The data: ", sample_tr)

    # Label Encoding
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(data)
    print("Label Encoded:", integer_encoded)

    # One-Hot Encoding
    onehot_encoder = OneHotEncoder()
    onehot_encoded = onehot_encoder.fit_transform(data).toarray()
    print("Onehot Encoded Matrix:\n", onehot_encoded)
if __name__ == '__main__':
    Read_file()
    one_hot()