def preprocess_input(data):
    processed_data = {
        'age': data['age'],
        'bmi': data['bmi'],
        'children': data['children'],
        'sex_male': 1 if data['sex'] == 'male' else 0,
        'smoker_yes': 1 if data['smoker'] == 'yes' else 0,
        'region_northwest': 1 if data['region'] == 'northwest' else 0,
        'region_southeast': 1 if data['region'] == 'southeast' else 0,
        'region_southwest': 1 if data['region'] == 'southwest' else 0,
    }
    
    return processed_data