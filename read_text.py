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
from konoise import NoiseGenerator

gen = NoiseGenerator(num_cores=8)
noise = ["disattach-letters", "change-vowels", "linking", "liquidization", "nasalization", "assimilation"]

if DEBUG and False:
    for key,value in kor.corpus_list().items():
        print(key, value)

corpus = knl()

texts = [c.pair for c in corpus.snli_train if not re.compile('[ㄱ-ㅎㅏ-ㅣa-zA-Z0-9一-龥]').search(c.pair)]
# noise_texts = [gen.generate(t, n, 0.5) for t in texts for n in noise]

a = gen.generate(texts[0], noise[0], 0.5, use_rust_tokenizer=True)

if DEBUG:
    idx = 0
    # for t in texts[0:50]:
    #     # print("#", idx, corpus.snli_train[idx].pair)
    #     print("*", idx, t)
    #     idx = idx + 1

    # for t in noise_texts[0:50]:
    #     # print("#", idx, corpus.snli_train[idx].pair)
    #     print("*", idx, t)
    #     idx = idx + 1


# a = re.compile('[ㄱ-ㅎㅏ-ㅣa-zA-Z0-9一-龥]').match(texts[26])
# print(a, texts[26])