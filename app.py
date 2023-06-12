from flask import Flask, request, json, jsonify
import os, sys
sys.path.append(os.path.abspath(".\\ChinJiIn\\chinjiin"))
import ChinJiIn.chinjiin.chinjiin as chinjiin 

# https://github.com/tjwjdgus12/ChinJiIn

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/fixer", methods=['GET'])
def test():
    sentence = request.args.get('sentence')
    words = sentence.split(' ')
    fixed_words = []
    print("data: {}".format(words))

    for w in words:
        fixed_represents = chinjiin.word_fixer.more_fix(w)
        fixed_word = chinjiin.fix(w)
        print("fixed word: {}".format(fixed_word))
        print("represents: {}".format(fixed_represents))
        fixed_words.append(fixed_word)
    print("data: {}".format(fixed_words))

    fixed_sentence = str.join(' ', fixed_words)
    print(fixed_represents)
    response = {
        "result": "ok",
        "fixed": fixed_sentence,
    }

    return fixed_sentence


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

