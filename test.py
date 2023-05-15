import random
from jamo import h2j, j2hcj
from unicode import join_jamos, split_syllables
import re

def disattachLetters(sentence: str, prob = 0.07):
    res = ""

    for idx in range(len(sentence)): 
        syl = j2hcj(h2j(sentence[idx])) if random.random() < prob else sentence[idx]  
        res += syl

    return res

def addLetter(sentence: str, prob = 0.07):
    res = ""

    for idx in range(len(sentence)): 
        
        syl = ""
        if random.random() < prob:
            tmp = j2hcj(h2j(sentence[idx]))
            num = random.randint(0, len(tmp))

            for j in range(len(tmp)):
                syl += tmp[j]
                if j == num: syl += tmp[j]
        else:
            syl = sentence[idx]   
        res += syl

    return res

def eraseLetter(sentence: str, prob = 0.1):
    res = ""

    for idx in range(len(sentence)): 
        
        syl = ""
        if random.random() < prob:
            tmp = j2hcj(h2j(sentence[idx]))
            num = random.randint(0, len(tmp))

            for j in range(len(tmp)):
                if j == num: continue
                syl += tmp[j]
        else:
            syl = sentence[idx]   
        res += syl

    return res

def liquidization(sentence:str, prob = 0.5):
    # Replace final consonants with their corresponding liquids
    res = ""
    liquids = {'ㄱ': 'ㄹ', 'ㄷ': 'ㄹ', 'ㅂ': 'ㅁ', 'ㅅ': 'ㄹ', 'ㅈ': 'ㄹ'}
    idx = 0
    for char in sentence:
        syl = j2hcj(h2j(char))
        last_s = syl[-1]
        if last_s in liquids and random.random() > prob:
            syl = syl[:-1] + liquids[last_s]
        res += join_jamos(syl)
        idx+=1

    return res

def changeVowels(sentence, prob = 0.5):
    neutral_vowels = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ']
    noisy_sentence = ""

    for char in sentence:
        syl = j2hcj(h2j(char))
        if len(syl) < 2:
            noisy_sentence += join_jamos(syl)
            continue
        if syl[1] in neutral_vowels and random.random() > prob:
            # Generate a random vowel for non-neutral characters
            vowel = random.choice(['ㅏ', 'ㅓ', 'ㅗ', 'ㅜ', 'ㅡ'])
            syl = syl[0] + vowel + syl[2:]
        noisy_sentence += join_jamos(syl)

    return noisy_sentence


def generate_noise(text):
    noise_text = ""
    for i in range(len(text)):
        if i < len(text) - 1 and text[i].isalpha() and text[i+1].isalpha():
            first_char, second_char = text[i], text[i+1]
            if ord(first_char) >= 0xAC00 and ord(first_char) <= 0xD7A3 and ord(second_char) >= 0xAC00 and ord(second_char) <= 0xD7A3:
                jamo_text1 = split_syllables(first_char)
                jamo_text2 = split_syllables(second_char)
                if jamo_text1[-1] == " ":
                    jamo_text1 = jamo_text1[:-2] + "ㄹ"
                noise_text += join_jamos(jamo_text1) + join_jamos(jamo_text2[1:])
                continue
        noise_text += text[i]
    return noise_text



def add_noise(sentence):
    # Apply liquidization to the sentence
    print("#0:", sentence)
    print("#1:", liquidization(sentence))
    print("#2:", changeVowels(sentence))
    print("#3:", disattachLetters(sentence))
    print("#4:", addLetter(sentence))
    print("#5:", eraseLetter(sentence))
    
    


# Example usage
sentence = "행복한 가정은 모두가 닮았지만, 불행한 가정은 모두 저마다의 이유로 불행하다."
add_noise(sentence)
