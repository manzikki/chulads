import datetime
import json
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET'])
def output_date():
    timenow = datetime.datetime.now()
    response = {'time': timenow }
    return jsonify(response), 200

app.run(host='127.0.0.1', port=5000)
