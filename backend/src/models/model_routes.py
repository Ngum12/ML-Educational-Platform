from flask import Blueprint, request, jsonify
import joblib  # For loading models

model_bp = Blueprint('model_bp', __name__)

# Assuming you have a pre-trained model saved in a file
MODEL_PATH = 'path/to/your/model.pkl'

@model_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    model = joblib.load(MODEL_PATH)
    prediction = model.predict([data['input']])
    return jsonify({'prediction': prediction.tolist()})

