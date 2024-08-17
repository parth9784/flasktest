from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    result = {
        "Addition": a + b
    }
    return jsonify(result)

@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    if b == 0:
        result = {"error": "Cannot divide by zero"}
    else:
        result = {
            "Divide": a / b
        }
    return jsonify(result)

@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    result = {
        "Multiply": a * b
    }
    return jsonify(result)

@app.route("/sub", methods=["POST"])
def sub():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    result = {
        "Subtraction": a - b
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
