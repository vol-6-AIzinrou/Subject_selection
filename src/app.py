from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/selectedOption', methods=['POST'])
def handle_selected_option():
    selectedOption = request.get_json()
    print("Received selectedOption: ", selectedOption)
    return jsonify(selectedOption), 200

if __name__ == '__main__':
    app.run(port=5000)
