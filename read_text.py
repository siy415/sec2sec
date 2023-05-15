# 말뭉치 위치
# https://ko-nlp.github.io/Korpora/ko-docs/corpuslist/kornli.html
# https://corpus.korean.go.kr/boards/faqList.do
# 노이즈 추가
# https://pypi.org/project/konoise/
# 오타 개선 패키지
# https://wikidocs.net/92961
# https://hleecaster.com/speller-cs-pusan-ac-kr/

import sys, re

DEBUG = True

from Korpora import Korpora as kor, KorNLIKorpus as knl

from test import *

noise = ["disattach-letters", "change-vowels", "linking", "liquidization", "nasalization", "assimilation"]

if DEBUG and False:
    for key,value in kor.corpus_list().items():
        print(key, value)

corpus = knl()

corpus_list = {"train": corpus.snli_train, "test": corpus.xnli_test}

for key, corpus_set in corpus_list.items():
    texts = [c.pair for c in corpus_set if not re.compile('[ㄱ-ㅎㅏ-ㅣa-zA-Z0-9一-龥]').search(c.pair)]
    dataset = ""
    for idx in range(len(texts)):
        add_letter = addLetter(texts[idx])
        erase_letter = eraseLetter(texts[idx])
        disattach_letter = disattachLetters(texts[idx])
        changed_letter = changeVowels(texts[idx])
        liquidizated_letter = liquidization(texts[idx])

        dataset += add_letter + '\t' + texts[idx] + '\n' if add_letter != texts[idx] else ''
        dataset += erase_letter + '\t' + texts[idx] + '\n' if erase_letter != texts[idx] else ''
        dataset += disattach_letter + '\t' + texts[idx] + '\n' if disattach_letter != texts[idx] else ''
        dataset += changed_letter + '\t' + texts[idx] + '\n' if changed_letter != texts[idx] else ''
        dataset += liquidizated_letter + '\t' + texts[idx] + '\n' if liquidizated_letter != texts[idx] else ''

        if idx % 10000 == 0: 
            print("--------[{}] generating noises[{}/{}({:.2f}%)]-------------".format(key, idx, len(texts), idx/len(texts)*100))
            print("original:         ", texts[idx])
            print("addLetter:        ", add_letter)
            print("eraseLetter:      ", erase_letter)
            print("disattachLetters: ", disattach_letter)
            print("changeVowels:     ", changed_letter)
            print("liquidization:    ", liquidizated_letter)

    print("--------generating {} dataset---------".format(key))
    f = open(".\{}.txt".format(key), 'w')
    f.write(dataset)