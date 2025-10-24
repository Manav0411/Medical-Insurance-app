import pytest
from app.services.inference import load_model, make_prediction

def test_load_model():
    model = load_model('models/insurance_model.pkl')
    assert model is not None

def test_make_prediction():
    model = load_model('models/insurance_model.pkl')
    sample_input = {
        'age': 30,
        'sex': 'male',
        'bmi': 25.0,
        'children': 1,
        'smoker': 'no',
        'region': 'southeast',
        'bmi_age': 750.0,
        'smoker_bmi': 0.0,
        'age_squared': 900,
        'bmi_squared': 625
    }
    prediction = make_prediction(model, sample_input)
    assert isinstance(prediction, float)
    assert prediction >= 0