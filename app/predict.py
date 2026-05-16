import joblib
import numpy as np

# Load model
model = joblib.load("../models/random_forest_model.pkl")

def predict_grade(features):
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)

    return prediction

sample = [
    18,
    85,
    80,
    78,
    81,
    30,
    1,
    0,
    1,
    2,
    1,
    1,
    0,
    1,
    0,
    0,
    0
]

result = predict_grade(sample)

print(f'result:{result}')

encoder = joblib.load("../models/grade_encoder.pkl")
decoded = encoder.inverse_transform(result)

print(f'decoded:{decoded}')