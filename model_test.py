from model import *

def evaluateTestset(encoder, decoder, out_pairs, input_lang, output_lang):
    right = 0
    for pair in out_pairs:
        s1 = normalizeString(pair[0])
        s2 = normalizeString(pair[1])
        input_lang.addSentence(s1)
        output_lang.addSentence(s2)
        print('>', pair[0])
        print('=', pair[1])
        output_words, attentions = evaluate(encoder, decoder, s1, input_lang, output_lang)
        output_sentence = ' '.join(output_words)
        print('<', output_sentence)
        print('')

        if(output_sentence == pair[1]):
            right+=1

    acc = right/len(out_pairs)

    print("acc: {}%".format(acc*100))


        



encoder = torch.load('.\\encoder.pth')
decoder = torch.load('.\\decoder.pth')

file = ".\\data\\train.txt"
test_file = '.\\data\\test.txt'
input_lang, output_lang, pairs = prepareData(file, False)
i, o, out_pairs = prepareData(test_file, False)

input_lang = Lang('wrong')

evaluateTestset(encoder, decoder, out_pairs, input_lang, output_lang)
