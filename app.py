import sys
sys.stdout.reconfigure(encoding='utf-8')

from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]
    
    # Cargar el cliente de Gradio
    client = Client("https://lordcoffee-mixtral-chat.hf.space/--replicas/bz3y4/")
    
    # Realizar la predicción
    result = client.predict(message, api_name="/chat")
    
    # Verificar la respuesta de la API
    if isinstance(result, list) and len(result) > 0:
        result = result[0]
    
    # Asegurarse de que la respuesta es un string
    if not isinstance(result, str):
        result = str(result)
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
