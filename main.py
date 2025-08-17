# LEGION Delta Command API (Flask-based, Render-ready)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Дозволяє виклики з ChatGPT

@app.route('/delta', methods=['POST'])
def delta():
    data = request.get_json()
    command = data.get("command")

    # Тут можна вставити логіку обробки Д-команд
    response = {
        "status": "OK",
        "received": command,
        "result": f"Команда '{command}' виконана. Вузол відповів."
    }
    return jsonify(response)

@app.route('/', methods=['GET'])
def index():
    return "LEGION Delta Node активний. Очікую Д-команду..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
