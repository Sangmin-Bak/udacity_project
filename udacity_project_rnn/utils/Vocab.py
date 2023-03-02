# import gzip
# import pandas as pd
# from nltk.stem.porter import *
# from nltk.stem import *
# from nltk.tokenize import RegexpTokenizer
# import nltk

SOS_token = 0
EOS_token = 1

class Vocab:
    def __init__(self, name):
        self.name = name
        self.word2index = {"SQS": SOS_token, "EOS": EOS_token}
        self.word2count = {}
        self.index2word = {SOS_token: "SOS", EOS_token: "EOS"}
        self.n_words = 2  # SOS 와 EOS 포함

    def addSentence(self, sentence):
        for word in sentence.split(" "):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1