import streamlit as st
import pickle5 as pickle
from transform_input import transform
import joblib

# Load model
with open("models/random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Student Performance Prediction")

# Inputs

age = st.number_input(
    "Enter Age",
    min_value=14,
    max_value=19,
    step=1
)

gender = st.selectbox(
    "Select Gender",
    ["Male", "Female", "Other"]
)

school_type = st.radio(
    "Select School Type",
    ["Private", "Public"]
)

parent_education = st.selectbox(
    "Parent Education Level",
    [
        "No formal",
        "High school",
        "Diploma",
        "Graduate",
        "Post graduate",
        "PhD"
    ]
)

study_hours = st.slider(
     "Study Hours per Day",
    min_value=0.5,
    max_value=8.0,
    step=0.5
)

attendance_percentage = st.slider(
     "Attendance Percentage",
    min_value=50.0,
    max_value=100.0,
    step=1.0
)

internet_access = st.radio(
    "Internet Access?",
    ["Yes", "No"]
)

travel_time = st.selectbox(
    "Travel Time",
    [
        "<15 min",
        "15-30 min",
        "30-60 min",
        ">60 min"
    ]
)

extra_activities = st.radio(
    "Extra Activities?",
    ["Yes", "No"]
)

study_method = st.selectbox(
    "Study Method",
    [
        "textbook",
        "notes",
        "online videos",
        "group study",
        "coaching",
        "mixed  "
    ]
)

math_score = st.number_input("Math Score",min_value=0,max_value=100)

science_score = st.number_input("Science Score",min_value=0,max_value=100)

english_score = st.number_input("English Score",min_value=0,max_value=100)

overall_score = st.number_input("Overall Score",min_value=0,max_value=100)

# Prediction
if st.button("Predict"):
    sample = transform(age, gender, school_type, parent_education, study_hours, attendance_percentage, internet_access, travel_time, extra_activities, study_method, math_score, science_score, english_score, overall_score)
    prediction = model.predict([sample])

    encoder = joblib.load('models/grade_encoder.pkl')
    decorded = encoder.inverse_transform(prediction)
    st.write('Predicted Final Grade:',decorded)