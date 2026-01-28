import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/receber", methods=["POST"])
def receber():
    dados = request.get_json(silent=True)

    logging.info("📍 DADOS RECEBIDOS:")
    logging.info(dados)

    return jsonify({"status": "ok"})

@app.route("/")
def home():
    return "Servidor ativo", 200
