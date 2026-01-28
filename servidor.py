from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/receber", methods=["POST"])
def receber():
    dados = request.get_json(silent=True)
    print("📍 Localização recebida:")
    print(dados)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
