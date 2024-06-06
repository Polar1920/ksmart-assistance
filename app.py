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
    # Carga del cliente fuera del bloque __name__ == "__main__"
    client = Client("PolarO3O/chat-efriend")
    result = client.predict(
        message=message,
        request=0.9,
        param_3=256,
        param_4=0.9,
        param_5=1.2,
        api_name="/chat"
    )
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
