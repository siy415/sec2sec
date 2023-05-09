import random
from jamo import h2j, j2hcj
from unicode import join_jamos
import re

def liquidization(sentence:str, th = 0.5):
    # Replace final consonants with their corresponding liquids
    res = ""
    liquids = {'ㄱ': 'ㄹ', 'ㄷ': 'ㄹ', 'ㅂ': 'ㅁ', 'ㅅ': 'ㄹ', 'ㅈ': 'ㄹ'}
    idx = 0
    for char in sentence:
        syl = j2hcj(h2j(char))
        last_s = syl[-1]
        if last_s in liquids and random.random() > th:
            syl = syl[:-1] + liquids[last_s]
        res += join_jamos(syl)
        idx+=1

    return res

def change_vowels(sentence, th = 0.5):
    neutral_vowels = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ']
    noisy_sentence = ""

    for char in sentence:
        syl = j2hcj(h2j(char))
        if len(syl) < 2:
            noisy_sentence += join_jamos(syl)
            continue
        if syl[1] in neutral_vowels and random.random() > th:
            # Generate a random vowel for non-neutral characters
            vowel = random.choice(['ㅏ', 'ㅓ', 'ㅗ', 'ㅜ', 'ㅡ'])
            syl = syl[0] + vowel + syl[2:]
        noisy_sentence += join_jamos(syl)

    return noisy_sentence


def add_noise(sentence):
    # Apply liquidization to the sentence
    print("#0:", sentence)
    print("#1:", liquidization(sentence))
    print("#2:", change_vowels(sentence))


# Example usage
sentence = "행복한 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이유로 불행하다."
add_noise(sentence)
