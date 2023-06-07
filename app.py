from flask import Flask, request, json, jsonify
# https://github.com/tjwjdgus12/ChinJiIn

app = Flask(__name__)

@app.route("/test", methods=['GET'])
def test():
    sentence = request.args.get('sentence')
    print("data: {}".format(sentence))

    response = {
        "result": "ok",
        "fixed": sentence,
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

