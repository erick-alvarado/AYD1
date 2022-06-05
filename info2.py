import json
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/resta', methods=['POST'])
def update_record():
    num1 = request.json['num1']
    num2 = request.json['num2']
    return jsonify({"resultado":num1-num2})
    


if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True)