from flask import Flask, request, jsonify
from flask_cors import CORS  # flask-corsをインポート
from make_response import Response
from make_reason import Reason


app = Flask(__name__)
CORS(app)  # CORSを許可

messages = None  # レスポンスデータを保持する変数

@app.route('/message', methods=['POST', 'GET'])
def handle_message():
    message = request.get_json()
    print("Received message: ", message)

    dialogueText = f"{message['id']}:{message['text']}"
    text_id = message['text']
    with open("history.txt", "a",  encoding="utf-8") as file:
        file.write(str(text_id)+ "\n")
    with open("dialogue.txt", "a", encoding="utf-8") as file:
        file.write(dialogueText+ "\n")

    messages = Response.make_response()
    print(messages)

    return jsonify(messages), 200

@app.route('/selectedOption', methods=['POST'])
def handle_selected_option():
    selectedOption = request.get_json()
    print("Received selectedOption: ", selectedOption)
    with open("option.txt", "w") as file:
        file.write(selectedOption['option'])

    return jsonify(selectedOption), 200

@app.route('/last', methods=['POST', 'GET'])
def handle_reason():
    message = request.get_json()
    print("Received message: ", message)

    dialogueText = f"{message['id']}:{message['text']}"
    text_id = message['text']
    with open("history.txt", "a",  encoding="utf-8") as file:
        file.write(str(text_id)+ "\n")
    with open("dialogue.txt", "a", encoding="utf-8") as file:
        file.write(dialogueText+ "\n")    

    message= [{'id': 1, 'text': '次に投票へ進みます'}]

    return jsonify(messages), 200

@app.route('/aimessage', methods=['GET'])
def aimessage():
    global messages
    # レスポンスが既に存在する場合は、再取得せずに前回の値を返す
    if messages is not None:
        return jsonify(messages)

    # レスポンスを生成し、messagesに格納
    messages = Response.make_response()
    print(messages)
    return jsonify(messages)

if __name__ == '__main__':
    app.run(port=5000)
