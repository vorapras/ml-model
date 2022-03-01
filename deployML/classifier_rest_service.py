from flask import Flask, request, make_response, jsonify
import pickle
import numpy as np

local_classifier = pickle.load(open('classifier.pickle','rb'))
local_scaler = pickle.load(open('sc.pickle','rb'))

app = Flask(__name__)

@app.route('/model',methods=['POST'])

def hello_world():
    request_data = request.get_json(force=True)
    age = request_data['age']
    salary = request_data['salary']
    pred = local_classifier.predict(local_scaler.transform(np.array([[age,salary]])))
    response = make_response(jsonify({"pred_res": str(pred)}))
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == "__main__":
    app.run(port=8000, debug=True)
