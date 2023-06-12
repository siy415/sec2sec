import os, sys
import os, sys
sys.path.append(os.path.abspath(".\\ChinJiIn\\chinjiin"))
import ChinJiIn.chinjiin.chinjiin as chinjiin



sentence = "다시 만난 세게"
words = sentence.split(' ')
fixed_words = []
print(words)

for w in words:
    fixed_represents = chinjiin.word_fixer.more_fix(w)
    fixed_word = chinjiin.fix(w)
    print(fixed_word)
    print(fixed_represents)
    fixed_words.append(fixed_word)

print(fixed_words)