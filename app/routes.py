from flask import Blueprint, render_template, request, jsonify
from app.services.inference import predict_insurance

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', prediction=None)

@main.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            form_data = request.get_json()
            prediction = predict_insurance(form_data)
            return jsonify({'predicted_charges': prediction})
        else:
            form_data = request.form.to_dict()
            prediction = predict_insurance(form_data)
            return render_template('index.html', prediction=prediction)

    except Exception as e:
        if request.is_json:
            return jsonify({'error': str(e)}), 500
        return render_template('index.html', prediction=None, error=f"Error: {str(e)}")