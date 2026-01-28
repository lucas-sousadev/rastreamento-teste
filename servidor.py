from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/receber", methods=["POST"])
def receber():
    dados = request.json
    print("Dados recebidos:")
    print(dados)
    return jsonify({"status": "ok"})

app.run(host="0.0.0.0", port=5000)