from flask import Flask 
from flask import jsonify
from flask import request
from flask_restful import Resource
from flask_cors import CORS, cross_origin
from flask_restful import Api

app = Flask(__name__)
cors = CORS (app)
app.config['CORS HEADERS'] = 'Content-Type'
api = Api (app)

# TODO add endpoints here

# this endpoint receives market data
@app.route('/market_data', methods=['POST'])
def post_data():
    data = request.json
    print("Received JSON data:", data)
    return data
    # return jsonify({"message": "Data received successfully"}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=105, debug=True)


