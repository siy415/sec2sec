
# https://choice-life.tistory.com/23

from __future__ import unicode_literals, print_function, division
from io import open
import unicodedata
import string
import re
import random

from common import *

line = ["안녕하십니ㄲㅏ\t안녕하십니까", "안녕히가세아\t안녕하가세요"]

pairs = [[s for s in l.split('\t')] for l in line]
print(pairs)

class Lang:
    def __init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2count = {}
        self.index2word = {0: "SOS", 1: "EOS"}
        self.n_words = 2  # SOS 와 EOS 포함

    def addSentence(self, sentence):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1

def readLangs(file:str, reverse=False):
    print("Reading lines...")

    # 파일을 읽고 줄로 분리
    lines = open(file, encoding='utf-8').read().strip().split('\n')

    # 모든 줄을 쌍으로 분리하고 정규화
    pairs = [[normalizeString(s) for s in l.split('\t')] for l in lines]

    # 쌍을 뒤집고, Lang 인스턴스 생성
    if reverse:
        pairs = [list(reversed(p)) for p in pairs]
        input_lang = Lang('wrong')
        output_lang = Lang('right')
    else:
        input_lang = Lang('wrong')
        output_lang = Lang('right')

    return input_lang, output_lang, pairs

def normalizeString(s):
    s = unicodeToAscii(s.strip())
    s = re.sub(r"([.!?])", r" \1", s)
    return s

# 유니 코드 문자열을 일반 ASCII로 변환하십시오.
# https://stackoverflow.com/a/518232/2809427
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

def filterPair(p):
    return len(p[0].split(' ')) < MAX_LENGTH and \
        len(p[1].split(' ')) < MAX_LENGTH


def filterPairs(pairs):
    return [pair for pair in pairs if filterPair(pair)]


def prepareData(file:str, reverse=False):
    input_lang, output_lang, pairs = readLangs(file, reverse)
    print("Read %s sentence pairs" % len(pairs))
    pairs = filterPairs(pairs)
    print("Trimmed to %s sentence pairs" % len(pairs))
    print("Counting words...")
    for pair in pairs:
        input_lang.addSentence(pair[0])
        output_lang.addSentence(pair[1])
    print("Counted words:")
    print(input_lang.name, input_lang.n_words)
    print(output_lang.name, output_lang.n_words)
    return input_lang, output_lang, pairs

if __name__ == "__main__":
    file = ".\\data\\train.txt"
    input_lang, output_lang, pairs = prepareData(file)
    print(random.choice(pairs))