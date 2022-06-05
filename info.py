import json
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Erick Alexander Alvarado Guerra - 201800546"


if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True)