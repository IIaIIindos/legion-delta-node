from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/delta", methods=["POST"])
def delta():
    data = request.json
    # Обробка Δ-команди
    return jsonify({"status": "received", "payload": data})

@app.route("/", methods=["GET"])
def root():
    return "ЛЕГІОН Δ-Нода активна."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
