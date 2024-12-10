from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
with open("GB.pkl", "rb") as f:
    GB_pickled_model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return "Hello, Flask is up and running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = data['features']
    prediction = GB_pickled_model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
