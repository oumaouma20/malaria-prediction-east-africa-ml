import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('random_forest_model.pkl') 

# Title
st.title("Malaria Incidence Predictor")

# Input form
year = st.number_input("Enter Year", min_value=2000, max_value=2025, value=2020)
prev_cases = st.number_input("Enter Previous Year Cases", min_value=0.0, value=100.0)
rainfall = st.number_input("Enter Rainfall Amount (mm)", min_value=0.0, value=120.0)
temperature = st.number_input("Enter Temperature (°C)", min_value=10.0, max_value=45.0, value=28.0)


# Prediction
if st.button("Predict"):
    input_df = pd.DataFrame({
        'Year': [year],
        'Cases_Previous': [cases],
        'Rainfall': [rainfall],
        'Temperature': [temperature]
    })
    prediction = model.predict(input_df)
    st.success(f"Predicted Malaria Incidence: {prediction[0]:.2f}")
