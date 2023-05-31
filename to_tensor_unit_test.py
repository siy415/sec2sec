import random
from parse_dataset import *
from model import *

if __name__ == "__main__":
    file = ".\\data\\train.txt"
    input_lang, output_lang, pairs = prepareData(file, False)

    ran_pair = random.choice(pairs)
    right_sen = ran_pair[1]
    right_indexes = indexesFromSentence(output_lang, right_sen)
    print(right_sen)
    print(random.choice(right_indexes))
    print(output_lang.word2index["두"])

    wrong_sen = ran_pair[0]
    wrong_indexes = indexesFromSentence(input_lang, wrong_sen)
    print(wrong_sen)
    print(random.choice(wrong_indexes))
    print(input_lang.word2index["남자ㄱㅏ"])