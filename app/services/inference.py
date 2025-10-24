import joblib
import numpy as np
import pandas as pd
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL = joblib.load(os.path.join(base_dir, 'models', 'insurance_model.pkl'))
SCALER = joblib.load(os.path.join(base_dir, 'models', 'scaler.pkl'))
FEATURE_NAMES = joblib.load(os.path.join(base_dir, 'models', 'feature_names.pkl'))

def predict_insurance(form_data):
    age = int(form_data['age'])
    sex = form_data['sex']
    bmi = float(form_data['bmi'])
    children = int(form_data['children'])
    smoker = form_data['smoker']
    region = form_data['region']
    
    bmi_age = bmi * age
    smoker_bmi = bmi * (1 if smoker == 'yes' else 0)
    age_squared = age ** 2
    bmi_squared = bmi ** 2
    
    features = {
        'age': age,
        'bmi': bmi,
        'children': children,
        'bmi_age': bmi_age,
        'smoker_bmi': smoker_bmi,
        'age_squared': age_squared,
        'bmi_squared': bmi_squared,
        'sex_male': 1 if sex == 'male' else 0,
        'smoker_yes': 1 if smoker == 'yes' else 0,
        'region_northwest': 1 if region == 'northwest' else 0,
        'region_southeast': 1 if region == 'southeast' else 0,
        'region_southwest': 1 if region == 'southwest' else 0,
    }
    
    input_df = pd.DataFrame([features])
    input_df = input_df.reindex(columns=FEATURE_NAMES, fill_value=0)
    input_scaled = SCALER.transform(input_df)
    prediction = MODEL.predict(input_scaled)[0]
    
    return round(prediction, 2)


def load_model(path):
    return joblib.load(os.path.join(base_dir, path))

def make_prediction(model, sample_input):
    age = int(sample_input.get('age', 0))
    sex = sample_input.get('sex', 'male')
    bmi = float(sample_input.get('bmi', 0.0))
    children = int(sample_input.get('children', 0))
    smoker = sample_input.get('smoker', 'no')
    region = sample_input.get('region', '')

    bmi_age = float(sample_input.get('bmi_age', bmi * age))
    smoker_bmi = float(sample_input.get('smoker_bmi', bmi * (1 if smoker == 'yes' else 0)))
    age_squared = float(sample_input.get('age_squared', age ** 2))
    bmi_squared = float(sample_input.get('bmi_squared', bmi ** 2))

    features = {
        'age': age,
        'bmi': bmi,
        'children': children,
        'bmi_age': bmi_age,
        'smoker_bmi': smoker_bmi,
        'age_squared': age_squared,
        'bmi_squared': bmi_squared,
        'sex_male': 1 if sex == 'male' else 0,
        'smoker_yes': 1 if smoker == 'yes' else 0,
        'region_northwest': 1 if region == 'northwest' else 0,
        'region_southeast': 1 if region == 'southeast' else 0,
        'region_southwest': 1 if region == 'southwest' else 0,
    }

    input_df = pd.DataFrame([features])
    input_df = input_df.reindex(columns=FEATURE_NAMES, fill_value=0)
    input_scaled = SCALER.transform(input_df)
    pred = model.predict(input_scaled)[0]
    return float(round(pred, 2))